"""Studio helper — standard library only. Run from anywhere:

    python Automation/studio.py log 2.5 Tactica Engineering "match engine fix"
    python Automation/studio.py hours            # this week and the last 4 weeks
    python Automation/studio.py due              # Proposed/Open decisions by decide-by date (A-05)
    python Automation/studio.py inbox            # ideas and which are past the cooling-off period
    python Automation/studio.py weekly           # draft this week's note into Studio/Reviews (A-03)
    python Automation/studio.py backlog Sovereign                       # check Games/<Game>/seed/backlog.csv (A-23)
    python Automation/studio.py backlog Sovereign --apply --repo you/sovereign   # create GitHub issues, write URLs back

Learning (13 Learning System):
    python Automation/studio.py predict Sovereign hours "P1 playable" 80-120 hours "seed backlog"
    python Automation/studio.py actual P-003 140
    python Automation/studio.py calibration [--write]   # actual/predicted by kind; backlog vs logged hours

Marketing (14 Marketing and Sales Playbook):
    python Automation/studio.py link Tactica 1234560 youtube demo-2027-05 creator-name   # UTM link, recorded in Studio/Marketing/links.csv

Dashboard:
    python Automation/studio.py dashboard     # writes Studio/Dashboard/*.json for the Studio Board

Hats: Design, Engineering, Production, Marketing, Business, Community (02 §1).
Game: a folder name under Games/, or "Studio" for studio-level work.
"""
import csv, datetime as dt, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOURS = ROOT / "Studio" / "hours.csv"
REVIEWS = ROOT / "Studio" / "Reviews"
CONFIG = json.loads((ROOT / "Automation" / "config.json").read_text(encoding="utf-8"))
HATS = ["Design", "Engineering", "Production", "Marketing", "Business", "Community"]
TODAY = dt.date.today()


def week_start(d):
    return d - dt.timedelta(days=d.weekday())  # Monday


# ---------- hours (A-04) ----------
def read_hours():
    if not HOURS.exists():
        return []
    rows = []
    with HOURS.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                rows.append({**r, "date": dt.date.fromisoformat(r["date"]), "hours": float(r["hours"])})
            except (ValueError, KeyError):
                print(f"skipping bad hours row: {r}", file=sys.stderr)
    return rows


def cmd_log(args):
    if len(args) < 3:
        sys.exit("usage: log HOURS GAME HAT [note] [--date YYYY-MM-DD]")
    date = TODAY
    if "--date" in args:
        i = args.index("--date"); date = dt.date.fromisoformat(args[i + 1]); args = args[:i] + args[i + 2:]
    hours, game, hat, note = float(args[0]), args[1], args[2].capitalize(), " ".join(args[3:])
    games = {p.name for p in (ROOT / "Games").iterdir() if p.is_dir()} | {"Studio"}
    if game not in games:
        sys.exit(f"unknown game '{game}'. Known: {', '.join(sorted(games))}")
    if hat not in HATS:
        sys.exit(f"unknown hat '{hat}'. Use one of: {', '.join(HATS)}")
    new = not HOURS.exists()
    with HOURS.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "game", "hat", "hours", "note"])
        w.writerow([date.isoformat(), game, hat, hours, note])
    print(f"logged {hours}h {game}/{hat} on {date}")


def hours_summary():
    rows = read_hours()
    ws = week_start(TODAY)
    this = [r for r in rows if r["date"] >= ws]
    lines = []
    total = sum(r["hours"] for r in this)
    budget = CONFIG.get("weekly_hours_budget")
    lines.append(f"This week (from {ws}): {total:.1f} h" + (f" of {budget} h budget" if budget else " (no budget set — S-17)"))
    by = {}
    for r in this:
        by.setdefault(r["game"], {}).setdefault(r["hat"], 0.0)
        by[r["game"]][r["hat"]] += r["hours"]
    for g, hats in sorted(by.items()):
        lines.append(f"  {g}: " + ", ".join(f"{h} {v:.1f}" for h, v in sorted(hats.items())))
    weeks = []
    for k in range(1, 5):
        s = ws - dt.timedelta(weeks=k); e = s + dt.timedelta(days=7)
        weeks.append(sum(r["hours"] for r in rows if s <= r["date"] < e))
    logged_weeks = sum(1 for w in weeks if w > 0)
    lines.append(f"Last 4 full weeks: {', '.join(f'{w:.1f}' for w in reversed(weeks))} h"
                 f" — average {sum(weeks)/4:.1f} h/week"
                 + ("" if logged_weeks == 4 else f" (only {logged_weeks} of 4 weeks have entries: not yet a measured number)"))
    used = {r["hat"] for r in rows if r["date"] >= ws - dt.timedelta(weeks=4)}
    idle = [h for h in HATS if h not in used]
    if idle:
        lines.append("Hats with no hours in 5 weeks: " + ", ".join(idle))
    return lines


# ---------- decide-by watcher (A-05) ----------
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def scan_decisions():
    found = []
    for md in sorted(ROOT.rglob("*.md")):
        if "Templates" in md.parts:
            continue
        lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        header = None
        for line in lines:
            if not line.lstrip().startswith("|"):
                header = None; continue
            cells = split_row(line)
            low = [c.lower() for c in cells]
            if "status" in low and any(c.startswith("decide by") for c in low):
                dec = next((i for i, c in enumerate(low) if c.startswith(("decision", "question", "risk", "lesson"))), 1)
                header = {"id": 0, "decision": dec,
                          "due": next(i for i, c in enumerate(low) if c.startswith("decide by")),
                          "status": low.index("status")}
                continue
            if header is None or set(line.replace("|", "").strip()) <= set("-: "):
                continue
            if len(cells) <= max(header.values()):
                continue
            status = cells[header["status"]]
            if not status.lower().startswith(("proposed", "open")):
                continue
            m = DATE.search(cells[header["due"]])
            due = dt.date.fromisoformat(m.group()) if m else None
            found.append({"file": md.relative_to(ROOT).as_posix(), "id": cells[header["id"]],
                          "decision": re.sub(r"\*\*", "", cells[header["decision"]]),
                          "due": due, "due_text": cells[header["due"]], "status": status.split(" ")[0].rstrip("—").strip()})
    return found


def due_lines():
    soon = CONFIG.get("due_soon_days", 3)
    items = scan_decisions()
    over = [d for d in items if d["due"] and d["due"] < TODAY]
    near = [d for d in items if d["due"] and TODAY <= d["due"] <= TODAY + dt.timedelta(days=soon)]
    later = [d for d in items if d["due"] and d["due"] > TODAY + dt.timedelta(days=soon)]
    undated = [d for d in items if not d["due"]]
    out = []
    def block(title, ds):
        if ds:
            out.append(f"{title} ({len(ds)}):")
            for d in sorted(ds, key=lambda d: (d["due"] or dt.date.max, d["id"])):
                out.append(f"  {d['id']:<6} {d['due_text']:<18} {d['status']:<9} {d['decision'][:90]}  [{d['file']}]")
    block("OVERDUE", over); block(f"Due within {soon} days", near); block("Later", later); block("No date (needs one)", undated)
    return out or ["No Proposed or Open decisions found."]


# ---------- inbox ----------
def inbox_lines():
    days = CONFIG.get("cooling_off_days", 30)
    out = []
    for f in sorted((ROOT / "Inbox").glob("*.md")):
        m = DATE.match(f.name)
        if not m:
            out.append(f"  {f.name}: no date in file name (use 'YYYY-MM-DD title.md')"); continue
        age = (TODAY - dt.date.fromisoformat(m.group())).days
        text = f.read_text(encoding="utf-8", errors="replace")
        rounds = len(re.findall(r"\[[xX]\] [123] ", text))
        survey = f", survey {rounds}/3" if "Idea Brief" in f.name else ", idea card only"
        out.append(f"  {f.stem}: {age} days{survey} — " + ("ready for triage" if age >= days else f"cooling off, {days - age} days left"))
    return [f"Inbox: {len(out)} idea(s)"] + out


def portfolio_lines():
    out = []
    for d in sorted((ROOT / "Games").iterdir()):
        readme = d / "README.md"
        if readme.exists():
            m = re.search(r"^Stage:\s*(.+)$", readme.read_text(encoding="utf-8"), re.M)
            out.append(f"  {d.name}: {m.group(1).strip() if m else 'stage not set'}")
    return ["Portfolio:"] + out


def cmd_weekly(_):
    REVIEWS.mkdir(parents=True, exist_ok=True)
    path = REVIEWS / f"{TODAY.isoformat()} weekly.md"
    if path.exists():
        sys.exit(f"{path.name} already exists — edit it, or delete it to redraft.")
    fence = lambda ls: "```\n" + "\n".join(ls) + "\n```"
    body = f"""# Weekly review — {TODAY.isoformat()}

*Draft from `studio.py weekly`. Correct it, answer the blanks, then it is closed.*

## 1. Hours
{fence(hours_summary())}

## 2. Progress (per game in a slot)
{fence(portfolio_lines())}
- Milestone moved this week? ______

## 3. Decisions due
{fence(due_lines())}

## 4. Players
- Review digest: ______ (none until a game is live)

## 5. Ideas
{fence(inbox_lines())}
- New ideas are filed only; triage is monthly.

## 6. Learning
{fence(calibration_lines())}
- Session retros this week: ______ · Lessons to decide: see section 3

## 7. Neglected hat
- ______

**Next week's one thing:** ______
"""
    path.write_text(body, encoding="utf-8")
    print(f"drafted {path.relative_to(ROOT)}")


# ---------- seed backlog to GitHub issues (A-23) ----------
BACKLOG_COLS = ["id", "title", "system", "type", "milestone", "acceptance", "depends_on", "estimate_hours", "source", "issue"]
TYPES = {"spike": "S", "feature": "F", "test": "T", "tooling": "X"}


def cmd_backlog(args):
    if not args:
        sys.exit("usage: backlog GAME [--apply --repo OWNER/NAME]")
    game, apply = args[0], "--apply" in args
    repo = args[args.index("--repo") + 1] if "--repo" in args else None
    path = ROOT / "Games" / game / "seed" / "backlog.csv"
    if not path.exists():
        sys.exit(f"no backlog at {path.relative_to(ROOT)} — copy Templates/Seed Pack/backlog.csv there first")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != BACKLOG_COLS:
            sys.exit(f"columns must be exactly: {','.join(BACKLOG_COLS)}")
        rows = list(reader)
    problems, ids = [], [r["id"] for r in rows]
    for n, r in enumerate(rows, start=2):
        where = f"row {n} ({r['id'] or 'no id'})"
        if ids.count(r["id"]) > 1: problems.append(f"{where}: duplicate id")
        t = r["type"].strip().lower()
        if t not in TYPES: problems.append(f"{where}: type must be one of {', '.join(TYPES)}")
        elif not r["id"].startswith(TYPES[t] + "-"): problems.append(f"{where}: a {t} id should start with {TYPES[t]}-")
        for col in ("title", "acceptance", "milestone"):
            if not r[col].strip(): problems.append(f"{where}: {col} is empty")
        for d in r["depends_on"].split():
            if d not in ids: problems.append(f"{where}: depends on unknown id {d}")
        if r["estimate_hours"] and not re.fullmatch(r"\d+(\.\d+)?(-\d+(\.\d+)?)?", r["estimate_hours"].strip()):
            problems.append(f"{where}: estimate_hours should look like 4 or 4-8")
    blocked = [r["id"] for r in rows if any(d.startswith("S-") for d in r["depends_on"].split())]
    lo = sum(float(r["estimate_hours"].split("-")[0]) for r in rows if r["estimate_hours"].strip() and not problems)
    hi = sum(float(r["estimate_hours"].split("-")[-1]) for r in rows if r["estimate_hours"].strip() and not problems)
    print(f"{len(rows)} items: " + ", ".join(f"{sum(1 for r in rows if r['type'].strip().lower()==t)} {t}" for t in TYPES))
    if not problems:
        print(f"estimate (unmeasured): {lo:g}-{hi:g} hours; waiting on a spike: {', '.join(blocked) or 'none'}")
    if problems:
        print("PROBLEMS:"); [print("  " + p) for p in problems]; sys.exit(1)
    pending = [r for r in rows if not r["issue"].strip()]
    if not apply:
        print(f"{len(pending)} item(s) not yet issues. Re-run with --apply --repo OWNER/NAME to create them.")
        return
    if not repo: sys.exit("--apply needs --repo OWNER/NAME")
    if not shutil.which("gh"): sys.exit("GitHub CLI (gh) not found; install it and run 'gh auth login'")
    labels = {f"type:{r['type'].strip().lower()}" for r in pending} | {f"milestone:{r['milestone']}" for r in pending} | {f"system:{r['system']}" for r in pending if r["system"]}
    for lb in sorted(labels):
        subprocess.run(["gh", "label", "create", lb, "--repo", repo, "--force"], check=True, capture_output=True)
    for r in pending:
        body = (f"**Acceptance:** {r['acceptance']}\n\n**Depends on:** {r['depends_on'] or 'nothing'}\n"
                f"**Estimate (unmeasured):** {r['estimate_hours'] or '—'} h\n**Source:** {r['source']} (seed pack)\n")
        args_ = ["gh", "issue", "create", "--repo", repo, "--title", f"[{r['id']}] {r['title']}", "--body", body]
        for lb in (f"type:{r['type'].strip().lower()}", f"milestone:{r['milestone']}", f"system:{r['system']}" if r["system"] else None):
            if lb: args_ += ["--label", lb]
        r["issue"] = subprocess.run(args_, check=True, capture_output=True, text=True).stdout.strip()
        print(f"  {r['id']} -> {r['issue']}")
        with path.open("w", newline="", encoding="utf-8") as f:  # write after each, so a failure loses nothing
            w = csv.DictWriter(f, fieldnames=BACKLOG_COLS); w.writeheader(); w.writerows(rows)


# ---------- learning: predictions and calibration (13 §4) ----------
LEARN = ROOT / "Studio" / "Learning"
PRED = LEARN / "predictions.csv"
PRED_COLS = ["id", "date", "game", "kind", "what", "predicted", "actual", "unit", "source", "closed_on"]
KINDS = ["hours", "weeks", "size", "count", "rate", "money"]
SIZE = {"S": 1, "M": 2, "L": 3}


def num(v):
    """'150-200' -> 175.0, '12' -> 12.0, 'M' -> 2.0, '' -> None"""
    v = str(v).strip()
    if not v: return None
    if v.upper() in SIZE: return float(SIZE[v.upper()])
    parts = v.replace(",", "").split("-")
    try:
        nums = [float(x) for x in parts if x != ""]
    except ValueError:
        return None
    return sum(nums) / len(nums) if nums else None


def read_preds():
    if not PRED.exists(): return []
    with PRED.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_preds(rows):
    with PRED.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=PRED_COLS); w.writeheader(); w.writerows(rows)


def cmd_predict(args):
    if len(args) < 5:
        sys.exit('usage: predict GAME KIND "what" VALUE UNIT ["source"]   kinds: ' + ", ".join(KINDS))
    game, kind, what, value, unit = args[:5]
    if kind not in KINDS: sys.exit("kind must be one of: " + ", ".join(KINDS))
    if num(value) is None: sys.exit("value must be a number, a range like 80-120, or S/M/L")
    rows = read_preds()
    n = max([int(r["id"].split("-")[1]) for r in rows if r["id"].startswith("P-")] + [0]) + 1
    rows.append({"id": f"P-{n:03d}", "date": TODAY.isoformat(), "game": game, "kind": kind, "what": what,
                 "predicted": value, "actual": "", "unit": unit, "source": " ".join(args[5:]), "closed_on": ""})
    LEARN.mkdir(parents=True, exist_ok=True); write_preds(rows)
    print(f"P-{n:03d} logged: {game} {kind} '{what}' predicted {value} {unit}")
    f = factors().get(kind)
    if f: print(f"  your {kind} factor is {f[0]:.2f}x over {f[1]} predictions -> corrected ~{num(value)*f[0]:.1f} {unit}")


def cmd_actual(args):
    if len(args) < 2: sys.exit("usage: actual P-ID VALUE")
    rows = read_preds()
    for r in rows:
        if r["id"] == args[0]:
            if num(args[1]) is None: sys.exit("value must be a number or S/M/L")
            r["actual"], r["closed_on"] = args[1], TODAY.isoformat()
            write_preds(rows)
            ratio = num(args[1]) / num(r["predicted"]) if num(r["predicted"]) else None
            print(f"{r['id']} closed: predicted {r['predicted']}, actual {args[1]} {r['unit']}" + (f" (x{ratio:.2f})" if ratio else ""))
            return
    sys.exit(f"no prediction {args[0]}")


def factors():
    out = {}
    for k in KINDS:
        ratios = sorted(num(r["actual"]) / num(r["predicted"]) for r in read_preds()
                        if r["kind"] == k and num(r["actual"]) is not None and num(r["predicted"]))
        if ratios:
            out[k] = (ratios[len(ratios) // 2] if len(ratios) % 2 else (ratios[len(ratios)//2 - 1] + ratios[len(ratios)//2]) / 2, len(ratios))
    return out


def backlog_vs_hours():
    lines, logged = [], {}
    for r in read_hours():
        for item in re.findall(r"\[([SFTX]-\d+)\]", r.get("note", "")):
            logged[(r["game"], item)] = logged.get((r["game"], item), 0.0) + r["hours"]
    for bl in sorted((ROOT / "Games").glob("*/seed/backlog.csv")):
        game = bl.parent.parent.name
        with bl.open(newline="", encoding="utf-8") as f:
            items = list(csv.DictReader(f))
        pairs = [(i["id"], num(i["estimate_hours"]), logged.get((game, i["id"]))) for i in items]
        done = [(i, e, a) for i, e, a in pairs if e and a]
        if done:
            ratios = sorted(a / e for _, e, a in done)
            lines.append(f"  {game}: {len(done)} backlog item(s) with logged hours; median actual/estimate x{ratios[len(ratios)//2]:.2f}")
    return lines


def calibration_lines():
    preds = read_preds()
    closed = [r for r in preds if r["actual"].strip()]
    out = [f"Predictions: {len(preds)} logged, {len(closed)} closed, {len(preds) - len(closed)} open"]
    f = factors()
    for k in KINDS:
        if k in f:
            ratio, n = f[k]
            note = "correction factor in use" if n >= 5 else f"needs {5 - n} more before it's used"
            out.append(f"  {k}: median actual/predicted x{ratio:.2f} over {n} — {note}")
    if not f: out.append("  no closed predictions yet")
    bh = backlog_vs_hours()
    out += (["Backlog estimates vs logged hours:"] + bh) if bh else ["Backlog vs hours: no items logged yet (put [F-03] etc. in hour notes)"]
    return out


def cmd_calibration(args):
    lines = calibration_lines()
    print("\n".join(lines))
    if "--write" in args:
        sl = LEARN / "Standing Lessons.md"
        text = sl.read_text(encoding="utf-8")
        a, b = "<!-- calibration:start -->", "<!-- calibration:end -->"
        if a in text and b in text:
            f = factors()
            used = [f"- **{k}**: x{r:.2f} ({n} predictions) — multiply new {k} estimates by this" for k, (r, n) in f.items() if n >= 5]
            block = "\n".join(used) or "No kind has 5 closed predictions yet; estimates are uncorrected."
            text = text[:text.index(a) + len(a)] + f"\n*Updated {TODAY.isoformat()}.*\n{block}\n" + text[text.index(b):]
            sl.write_text(text, encoding="utf-8"); print("Standing Lessons calibration block updated")


# ---------- marketing: UTM links (14 M-13) ----------
LINKS = ROOT / "Studio" / "Marketing" / "links.csv"
SLUG = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def cmd_link(args):
    if len(args) < 4:
        sys.exit("usage: link GAME APPID SOURCE CAMPAIGN [CONTENT]   (lowercase, digits, . _ - only)")
    game, appid, source, campaign = args[:4]
    content = args[4] if len(args) > 4 else ""
    if not appid.isdigit(): sys.exit("APPID must be the numeric Steam app id")
    for name, v in (("source", source), ("campaign", campaign), ("content", content)):
        if v and not SLUG.match(v): sys.exit(f"{name} '{v}' must be lowercase letters, digits, . _ - (no spaces)")
    from urllib.parse import urlencode
    q = {"utm_source": source, "utm_campaign": campaign}
    if content: q["utm_content"] = content
    url = f"https://store.steampowered.com/app/{appid}/?{urlencode(q)}"
    LINKS.parent.mkdir(parents=True, exist_ok=True)
    new = not LINKS.exists()
    rows = []
    if not new:
        with LINKS.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    if any(r["url"] == url for r in rows):
        print(url + "   (already recorded)"); return
    with LINKS.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new: w.writerow(["date", "game", "appid", "source", "campaign", "content", "url"])
        w.writerow([TODAY.isoformat(), game, appid, source, campaign, content, url])
    print(url)


# ---------- dashboard export (Studio Board) ----------
DASH = ROOT / "Studio" / "Dashboard"


def md_table_rows(path, key_col):
    """Rows of the first markdown table whose header contains key_col, as dicts."""
    if not path.exists(): return []
    rows, header = [], None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.lstrip().startswith("|"):
            if header and rows: break
            header = None; continue
        cells = split_row(line)
        if header is None:
            if key_col in cells: header = cells
            continue
        if set(line.replace("|", "").strip()) <= set("-: "): continue
        if len(cells) == len(header): rows.append(dict(zip(header, cells)))
    return rows


def cmd_dashboard(args):
    DASH.mkdir(parents=True, exist_ok=True)
    out = {}
    # portfolio
    port = []
    for d in sorted((ROOT / "Games").iterdir()):
        r = d / "README.md"
        if not r.exists(): continue
        t = r.read_text(encoding="utf-8")
        m = re.search(r"^Stage:\s*(.+)$", t, re.M)
        open_, done = len(re.findall(r"^- \[ \]", t, re.M)), len(re.findall(r"^- \[[xX]\]", t, re.M))
        port.append({"game": d.name, "stage": m.group(1).strip() if m else "Not set", "owed_open": open_, "owed_total": open_ + done})
    out["portfolio"] = port
    # decisions
    soon_days = CONFIG.get("due_soon_days", 3)
    dec = []
    for x in scan_decisions():
        if x["due"] is None: bucket, days = "No date", None
        else:
            days = (x["due"] - TODAY).days
            bucket = "Overdue" if days < 0 else ("Due soon" if days <= soon_days else "Later")
        dec.append({"id": x["id"], "item": x["decision"], "status": x["status"], "decide_by": x["due"].isoformat() if x["due"] else x["due_text"],
                    "days_left": days, "bucket": bucket, "file": x["file"]})
    order = {"Overdue": 0, "Due soon": 1, "Later": 2, "No date": 3}
    dec.sort(key=lambda d: (order[d["bucket"]], d["days_left"] if d["days_left"] is not None else 9999, d["id"]))
    out["decisions"] = dec
    # hours per week (last 12 weeks), by game
    rows = read_hours(); ws = week_start(TODAY)
    games = sorted({r["game"] for r in rows} | {p["game"] for p in port} | {"Studio"})
    hw = []
    for k in range(11, -1, -1):
        s0 = ws - dt.timedelta(weeks=k); e0 = s0 + dt.timedelta(days=7)
        for g in games:
            hw.append({"week": s0.isoformat(), "game": g, "hours": round(sum(r["hours"] for r in rows if r["game"] == g and s0 <= r["date"] < e0), 2)})
    out["hours_weekly"] = hw
    # calibration
    f = factors()
    out["calibration"] = [{"kind": k, "factor": round(f[k][0], 2) if k in f else None, "closed": f[k][1] if k in f else 0,
                           "in_use": k in f and f[k][1] >= 5} for k in KINDS]  # every kind, so the file is never empty
    preds = read_preds()
    out["predictions_open"] = [{"id": r["id"], "game": r["game"], "kind": r["kind"], "what": r["what"], "predicted": r["predicted"], "unit": r["unit"], "logged": r["date"]}
                               for r in preds if not r["actual"].strip()]
    # lessons
    out["lessons"] = [{"id": r["ID"], "lesson": r["Lesson"], "game": r["Game"], "status": r["Status"], "seen": int(r["Seen"]) if r["Seen"].isdigit() else 0}
                      for r in md_table_rows(LEARN / "Lessons Register.md", "ID")]
    # inbox
    inbox = []
    days_cool = CONFIG.get("cooling_off_days", 30)
    for fpath in sorted((ROOT / "Inbox").glob("*.md")):
        m = DATE.match(fpath.name)
        if not m: continue
        age = (TODAY - dt.date.fromisoformat(m.group())).days
        text = fpath.read_text(encoding="utf-8", errors="replace")
        inbox.append({"idea": fpath.stem[11:].replace(" — Idea Brief", ""), "age_days": age,
                      "survey_rounds": len(re.findall(r"\[[xX]\] [123] ", text)), "ready_for_triage": age >= days_cool})
    out["inbox"] = inbox or [{"idea": "No ideas in the inbox", "age_days": None, "survey_rounds": None, "ready_for_triage": False, "placeholder": True}]
    # upcoming events from the festival calendar
    ev = []
    for r in md_table_rows(ROOT / "Studio" / "Marketing" / "Festival Calendar.md", "Event"):
        d = re.findall(r"(\d{4}-\d{2}-\d{2}|\d{2}-\d{2})", r.get("Dates", ""))
        if not d or len(d[0]) != 10: continue
        start = dt.date.fromisoformat(d[0])
        end = start
        if len(d) > 1: end = dt.date.fromisoformat(d[1] if len(d[1]) == 10 else f"{start.year}-{d[1]}")
        if end < TODAY: continue
        ev.append({"event": r["Event"], "start": start.isoformat(), "end": end.isoformat(), "deadline": r.get("Deadline", ""), "fit": r.get("Fit (Tactica / Sovereign)", "")})
    ev.sort(key=lambda e: e["start"])
    out["events"] = ev
    # summary (one row)
    this_week = sum(r["hours"] for r in rows if r["date"] >= ws)
    prev4 = [sum(r["hours"] for r in rows if ws - dt.timedelta(weeks=k) <= r["date"] < ws - dt.timedelta(weeks=k - 1)) for k in range(1, 5)]
    out["summary"] = [{
        "as_of": TODAY.isoformat(),
        "hours_this_week": round(this_week, 2), "hours_4wk_avg": round(sum(prev4) / 4, 2),
        "weeks_logged_of_4": sum(1 for w in prev4 if w > 0), "weekly_budget": CONFIG.get("weekly_hours_budget"),
        "decisions_waiting": sum(1 for x in dec if x["status"].lower().startswith(("proposed", "open")) and not x["id"].startswith("L-")),
        "overdue": sum(1 for x in dec if x["bucket"] == "Overdue"),
        "due_soon": sum(1 for x in dec if x["bucket"] == "Due soon"),
        "lessons_to_decide": sum(1 for l in out["lessons"] if l["status"].lower().startswith("proposed")),
        "ideas_in_inbox": len(inbox), "predictions_open": len(out["predictions_open"]),
        "predictions_closed": sum(1 for r in preds if r["actual"].strip()),
        "next_event": ev[0]["event"] if ev else None, "next_event_start": ev[0]["start"] if ev else None,
    }]
    for name, data in out.items():
        (DASH / f"{name}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"  {name}.json: {len(data)} row(s)")
    print(f"wrote Studio/Dashboard/ ({TODAY.isoformat()})")


COMMANDS = {
    "dashboard": cmd_dashboard,
    "link": cmd_link,
    "predict": cmd_predict,
    "actual": cmd_actual,
    "calibration": cmd_calibration,
    "backlog": cmd_backlog,
    "log": cmd_log,
    "hours": lambda a: print("\n".join(hours_summary())),
    "due": lambda a: print("\n".join(due_lines())),
    "inbox": lambda a: print("\n".join(inbox_lines())),
    "weekly": cmd_weekly,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    COMMANDS[sys.argv[1]](sys.argv[2:])
