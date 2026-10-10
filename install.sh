#!/usr/bin/env bash
# Копирует скилы в папку .claude/skills проекта (или ~/.claude/skills с -g).
# ./install.sh <путь-к-проекту> [скил ...]   — без списка ставятся все
# ./install.sh -g [скил ...]                 — глобально для Claude Code
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
if [ "${1:-}" = "-g" ]; then dest="$HOME/.claude/skills"; else dest="${1:?путь к проекту}/.claude/skills"; fi
shift
mkdir -p "$dest"
if [ $# -eq 0 ]; then set -- $(ls "$here/skills"); fi
for s in "$@"; do
  [ -f "$here/skills/$s/SKILL.md" ] || { echo "нет скила: $s" >&2; exit 1; }
  rm -rf "$dest/$s"; cp -r "$here/skills/$s" "$dest/$s"; echo "+ $s"
done
