#!/usr/bin/env python3
"""Добавляет скилы с GitHub (или из локальной папки) в эту библиотеку.

Пример:
  python3 tools/add-skill.py https://github.com/owner/repo --plugin gamedev
  python3 tools/add-skill.py https://github.com/owner/repo/tree/main/skills/foo --plugin dev-workflow
  python3 tools/add-skill.py owner/repo --plugin my-pack --agents --description "Что даёт плагин"
  python3 tools/add-skill.py ~/Downloads/some-skill --plugin gamedev
  python3 tools/add-skill.py owner/repo --list          # только показать, какие скилы там есть

Что делает:
  1. Клонирует репозиторий (git clone --depth 1) во временную папку.
  2. Находит все папки с SKILL.md (или только указанный --path / --only).
  3. Копирует их в plugins/<плагин>/skills/<имя-скила>/.
  4. С --agents копирует agents/*.md в plugins/<плагин>/agents/.
  5. Кладёт LICENSE/NOTICE источника в licenses/<repo>/.
  6. Если плагина ещё нет, создаёт plugins/<плагин>/.claude-plugin/plugin.json
     и дописывает плагин в .claude-plugin/marketplace.json.
  7. Запускает `claude plugin validate .` (если установлен Claude Code).
  8. Печатает строки для таблицы в README и что делать дальше (commit, push, PR).

Только стандартная библиотека Python 3.9+. Ничего не коммитит и не пушит.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
GITHUB_RE = re.compile(
    r"^(?:https?://)?(?:www\.)?github\.com/(?P<owner>[^/\s]+)/(?P<repo>[^/\s#?]+?)(?:\.git)?"
    r"(?:/(?:tree|blob)/(?P<ref>[^/\s]+)(?:/(?P<path>[^#?\s]*))?)?/?$"
)
SHORT_RE = re.compile(r"^(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)$")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}


def die(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"ошибка: {msg}", file=sys.stderr)
    sys.exit(1)


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    """Простой разбор YAML-шапки: name, description (в т.ч. свёрнутые > и |)."""
    lines = skill_md.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    key_re = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        m = key_re.match(lines[i])
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2).strip()
        if value in {">", "|", ">-", "|-", ">+", "|+"} or value == "":
            block: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != "---" and (not lines[i].strip() or lines[i][:1] in " \t"):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(block)
            continue
        fields[key] = value.strip("\"'")
        i += 1
    return fields


def resolve_source(source: str, ref: str | None) -> tuple[Path, Path | None, str, str | None]:
    """Возвращает (корень исходника, временная папка или None, подпись источника, подпуть)."""
    local = Path(source).expanduser()
    if local.exists():
        return local.resolve(), None, str(local.resolve()), None

    m = GITHUB_RE.match(source.strip())
    if m:
        owner, repo = m.group("owner"), m.group("repo")
        ref = ref or m.group("ref")
        sub = m.group("path") or None
    else:
        m = SHORT_RE.match(source.strip())
        if not m:
            die(f"не понимаю источник {source!r}: нужна ссылка на GitHub, owner/repo или существующая папка")
        owner, repo, sub = m.group("owner"), m.group("repo"), None

    url = f"https://github.com/{owner}/{repo}.git"
    tmp = Path(tempfile.mkdtemp(prefix="add-skill-"))
    cmd = ["git", "clone", "--quiet", "--depth", "1"]
    if ref:
        cmd += ["--branch", ref]
    cmd += [url, str(tmp / repo)]
    print(f"клонирую {url}" + (f" (ветка {ref})" if ref else "") + " …")
    try:
        subprocess.run(cmd, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        shutil.rmtree(tmp, ignore_errors=True)
        die(f"git clone не удался: {exc}")
    return tmp / repo, tmp, f"https://github.com/{owner}/{repo}", sub


def find_skills(root: Path) -> list[Path]:
    if (root / "SKILL.md").is_file():
        return [root]
    found: list[Path] = []
    for skill_md in sorted(root.rglob("SKILL.md")):
        if any(part in SKIP_DIRS for part in skill_md.relative_to(root).parts):
            continue
        found.append(skill_md.parent)
    return found


def find_agents(*roots: Path) -> list[Path]:
    """Агенты ищутся в agents/ и .claude/agents/ рядом со скилами и в корне источника."""
    agents: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        for folder in (root / "agents", root / ".claude" / "agents"):
            if folder.is_dir():
                for p in sorted(folder.glob("*.md")):
                    if p.resolve() not in seen and read_frontmatter(p).get("name"):
                        seen.add(p.resolve())
                        agents.append(p)
    return agents


def detect_license(*roots: Path) -> tuple[list[Path], str]:
    """LICENSE/NOTICE ищутся в корне источника, иначе в папке со скилами."""
    files: list[Path] = []
    for root in roots:
        files = [p for p in sorted(root.iterdir()) if p.is_file() and p.name.upper().startswith(("LICENSE", "LICENCE", "NOTICE", "COPYING"))]
        if files:
            break
    kind = "см. LICENSE"
    for p in files:
        head = p.read_text(encoding="utf-8", errors="replace")[:600].lower()
        if "mit license" in head:
            kind = "MIT"
        elif "apache license" in head:
            kind = "Apache-2.0"
        elif "gnu general public" in head:
            kind = "GPL"
        elif "creative commons" in head:
            kind = "CC"
        elif "bsd" in head:
            kind = "BSD"
        if kind != "см. LICENSE":
            break
    return files, kind


def copy_tree(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*SKIP_DIRS, ".DS_Store"))


def plugin_known(name: str) -> bool:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return any(p.get("name") == name for p in data.get("plugins", []))


def register_plugin(name: str, description: str, homepage: str, license_kind: str, dry: bool) -> None:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugin_dir = REPO_ROOT / "plugins" / name
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        payload = {"name": name, "displayName": name, "description": description, "author": data.get("owner", {})}
        if homepage.startswith(("http://", "https://")):
            payload["homepage"] = homepage
        payload["license"] = license_kind
        print(f"создаю {manifest.relative_to(REPO_ROOT)}")
        if not dry:
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not plugin_known(name):
        print(f"дописываю плагин {name!r} в {MARKETPLACE.relative_to(REPO_ROOT)}")
        data.setdefault("plugins", []).append(
            {"name": name, "source": f"./plugins/{name}", "description": description, "category": "skills"}
        )
        if not dry:
            MARKETPLACE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def count_library() -> tuple[int, int]:
    skills = len(list((REPO_ROOT / "plugins").glob("*/skills/*/SKILL.md")))
    plugins = len([p for p in (REPO_ROOT / "plugins").iterdir() if (p / ".claude-plugin" / "plugin.json").exists()])
    return skills, plugins


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="ссылка на GitHub (репозиторий или папка внутри него), owner/repo или локальная папка")
    ap.add_argument("--plugin", "-p", help="в какой плагин класть (plugins/<имя>); обязателен, если не --list")
    ap.add_argument("--path", help="подпапка внутри репозитория, где искать скилы")
    ap.add_argument("--ref", help="ветка или тег (по умолчанию ветка по умолчанию)")
    ap.add_argument("--only", nargs="+", metavar="SKILL", help="взять только эти скилы (имена папок)")
    ap.add_argument("--agents", action="store_true", help="также скопировать агентов (agents/*.md или .claude/agents/*.md)")
    ap.add_argument("--description", help="описание нового плагина для marketplace.json (по умолчанию 'Скилы из <источник>')")
    ap.add_argument("--force", action="store_true", help="перезаписать скил, если он уже есть в плагине")
    ap.add_argument("--list", action="store_true", help="только показать скилы и агентов источника, ничего не копировать")
    ap.add_argument("--dry-run", action="store_true", help="показать, что будет сделано, без записи")
    ap.add_argument("--no-validate", action="store_true", help="не запускать claude plugin validate")
    args = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)

    if not args.list and not args.plugin:
        ap.error("нужен --plugin <имя> (или --list)")
    if args.plugin and not NAME_RE.fullmatch(args.plugin):
        die("имя плагина: строчные латинские буквы, цифры и дефисы, например my-pack")

    root, tmp, source_label, sub = resolve_source(args.source, args.ref)
    try:
        search = root / (args.path or sub or "")
        if not search.exists():
            die(f"в источнике нет папки {search.relative_to(root)}")
        skills = find_skills(search)
        if args.only:
            wanted = set(args.only)
            skills = [s for s in skills if s.name in wanted or read_frontmatter(s / "SKILL.md").get("name") in wanted]
            missing = wanted - {s.name for s in skills} - {read_frontmatter(s / "SKILL.md").get("name", "") for s in skills}
            if missing:
                die(f"не нашёл скилы: {', '.join(sorted(missing))}")
        agents = find_agents(search, root) if (args.agents or args.list) else []
        if not skills and not agents:
            die("не нашёл ни одного SKILL.md (попробуй --path или проверь ссылку)")

        print(f"\nисточник: {source_label}")
        print(f"скилов: {len(skills)}" + (f", агентов: {len(agents)}" if agents else ""))
        for s in skills:
            fm = read_frontmatter(s / "SKILL.md")
            print(f"  {fm.get('name') or s.name:32} {fm.get('description', '')[:90]}")
        if agents:
            for a in agents:
                print(f"  [агент] {a.stem:24} {read_frontmatter(a).get('description', '')[:80]}")
        if args.list:
            return 0

        dry = args.dry_run
        plugin_dir = REPO_ROOT / "plugins" / args.plugin
        rows: list[str] = []
        added = skipped = 0
        for s in skills:
            fm = read_frontmatter(s / "SKILL.md")
            name = fm.get("name") or s.name
            if not NAME_RE.fullmatch(name):
                print(f"  ! пропускаю {s.name}: имя {name!r} не подходит (нужны строчные буквы, цифры, дефисы)")
                skipped += 1
                continue
            if name != s.name:
                print(f"  ~ {s.name}: в шапке name: {name}, кладу в папку {name}")
            dst = plugin_dir / "skills" / name
            if dst.exists() and not args.force:
                print(f"  = {name}: уже есть, пропускаю (перезаписать: --force)")
                skipped += 1
                continue
            print(f"  + {dst.relative_to(REPO_ROOT)}")
            if not dry:
                if dst.exists():
                    shutil.rmtree(dst)
                copy_tree(s, dst)
            rows.append(f"| `{name}` | {fm.get('description', '').replace('|', '/')} |")
            added += 1

        if args.agents:
            for a in agents:
                dst = plugin_dir / "agents" / a.name
                if dst.exists() and not args.force:
                    print(f"  = агент {a.stem}: уже есть, пропускаю")
                    continue
                print(f"  + {dst.relative_to(REPO_ROOT)}")
                if not dry:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(a, dst)

        license_files, license_kind = detect_license(root, search)
        repo_slug = source_label.rstrip("/").split("/")[-1].lower()
        lic_dir = REPO_ROOT / "licenses" / repo_slug
        if license_files and not lic_dir.exists():
            print(f"  + {lic_dir.relative_to(REPO_ROOT)}/ ({', '.join(p.name for p in license_files)}; {license_kind})")
            if not dry:
                lic_dir.mkdir(parents=True)
                for p in license_files:
                    shutil.copy2(p, lic_dir / p.name)
        elif not license_files:
            print("  ! в источнике нет файла LICENSE: проверь, можно ли его использовать")

        description = args.description or f"Скилы из {source_label}"
        register_plugin(args.plugin, description, source_label, license_kind, dry)

        total_skills, total_plugins = count_library()
        print(f"\nдобавлено скилов: {added}, пропущено: {skipped}")
        print(f"в библиотеке теперь: {total_skills} скилов в {total_plugins} плагинах (обнови цифры в README.md)")
        if rows:
            print(f"\nстроки для таблицы «### {args.plugin}» в README.md:")
            print("\n".join(rows))

        if not dry and not args.no_validate and shutil.which("claude"):
            print("\nпроверка: claude plugin validate .")
            subprocess.run(["claude", "plugin", "validate", "."], cwd=REPO_ROOT)

        print(
            "\nдальше:\n"
            "  git checkout -b add-<имя>   # новая ветка\n"
            "  git add -A && git commit -m \"Add <имя> skills\"\n"
            "  git push -u origin add-<имя>   # и открыть PR в ветку по умолчанию\n"
            "после слияния: claude.ai → Customize → Plugins → маркетплейс iliafreedive-skills → Check for updates\n"
            "(новый плагин там нужно один раз нажать Add)."
        )
        return 0
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
