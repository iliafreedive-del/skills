import os, re, sys, zipfile, json
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
ALLOWED = {"name","description","license","allowed-tools","metadata","compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
report = []
for d in sorted(os.listdir(src)):
    p = os.path.join(src, d, "SKILL.md")
    if not os.path.isfile(p): continue
    text = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    errs = []
    if not m: print("NO FRONTMATTER", d); continue
    fm = m.group(1).split("\n")
    # top-level keys
    keys = [re.match(r"^([A-Za-z_-]+):", l).group(1) for l in fm if re.match(r"^[A-Za-z_-]+:", l)]
    newfm, extra, skip = [], {}, False
    for l in fm:
        k = re.match(r"^([A-Za-z_-]+):\s*(.*)$", l)
        if k:
            skip = k.group(1) not in ALLOWED
            if skip: extra[k.group(1)] = k.group(2).strip().strip('"\''); continue
        elif skip: continue
        newfm.append(l)
    if extra:
        if "metadata" in keys:
            i = next(i for i,l in enumerate(newfm) if l.startswith("metadata:"))
            for kk,v in extra.items(): newfm.insert(i+1, f"  {kk}: {json.dumps(v, ensure_ascii=False)}")
        else:
            newfm.append("metadata:")
            for kk,v in extra.items(): newfm.append(f"  {kk}: {json.dumps(v, ensure_ascii=False)}")
    nm = next((re.match(r"^name:\s*(.*)$",l).group(1).strip().strip('"\'') for l in newfm if l.startswith("name:")), "")
    # description may be multi-line (>, |) - reconstruct roughly
    di = next(i for i,l in enumerate(newfm) if l.startswith("description:"))
    dv = newfm[di].split(":",1)[1].strip()
    if dv in (">", "|", ">-", "|-", ""):
        j=di+1; parts=[]
        while j < len(newfm) and (newfm[j].startswith(" ") or not newfm[j].strip()): parts.append(newfm[j].strip()); j+=1
        dv = " ".join(parts)
    j0 = di+1
    if newfm[di].split(":",1)[1].strip() in (">", "|", ">-", "|-", ""):
        while j0 < len(newfm) and (newfm[j0].startswith(" ") or not newfm[j0].strip()): j0+=1
    if len(dv)>1 and dv[0]==dv[-1] and dv[0] in "\"'": dv = dv[1:-1]
    newfm[di:j0] = ["description: " + json.dumps(dv, ensure_ascii=False)]
    if not NAME_RE.match(nm) or len(nm)>64: errs.append("bad name "+nm)
    if "claude" in nm or "anthropic" in nm: errs.append("reserved word in name")
    if nm != d: errs.append(f"name {nm} != folder {d}")
    if not dv or len(dv)>1024: errs.append(f"description len {len(dv)}")
    if "<" in dv or ">" in dv: errs.append("angle brackets in description")
    newtext = "---\n" + "\n".join(newfm) + "\n---\n" + text[m.end():]
    zp = os.path.join(out, nm + ".zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(os.path.join(src, d)):
            dirs[:] = [x for x in dirs if x not in (".git","__pycache__","node_modules",".DS_Store")]
            for f in files:
                if f in (".DS_Store",) or f.endswith(".pyc"): continue
                fp = os.path.join(root, f)
                if os.path.islink(fp): errs.append("symlink "+fp); continue
                arc = os.path.join(nm, os.path.relpath(fp, os.path.join(src, d)))
                if os.path.relpath(fp, os.path.join(src,d)) == "SKILL.md": z.writestr(arc, newtext)
                else: z.write(fp, arc)
    report.append((nm, os.path.getsize(zp), extra, errs))
    if errs or extra: print(nm, extra, errs)
print(len(report), "zips", sum(r[1] for r in report)//1024, "KB")
