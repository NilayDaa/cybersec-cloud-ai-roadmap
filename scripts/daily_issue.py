#!/usr/bin/env python3
"""Daily issue engine.

State model (git-tracked file .study-progress.json):
    { "last_date": "YYYY-MM-DD", "current_day": N }

On each run:
  - If today != last_date, advance current_day by 1 (clamp to total_days).
  - Ensure an issue exists for current_day (create if missing).
  - Close any stale open daily-study issues from earlier days.
  - Commit the state file only when it changed.

Idempotent: re-running the same date does not double-open or re-advance.
The engine keeps working after this repo is forked by the user.
"""
import json, os, subprocess, sys
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(REPO, ".study-progress.json")
SCHED = os.path.join(REPO, "schedule.json")
GH = "gh"
DRY = "--dry-run" in sys.argv

def run(*args, **kw):
    if DRY:
        print("DRY:", " ".join(str(a) for a in args)); return ""
    return subprocess.run([str(a) for a in args], capture_output=True, text=True, **kw)

def gh_call(*args):
    if DRY:
        print("DRY: gh", " ".join(str(a) for a in args)); return "[]"
    r = run(GH, *args, cwd=REPO)
    if r.returncode != 0:
        print(f"gh error: {r.stderr.strip() or r.stdout.strip()}", file=sys.stderr)
    return r.stdout.strip()

def main():
    sched = json.load(open(SCHED))
    total = sched["total_days"]
    days = {d["day"]: d for d in sched["days"]}

    # ---- load / init state ----
    if os.path.exists(STATE_FILE):
        state = json.load(open(STATE_FILE))
    else:
        state = {"last_date": None, "current_day": 0}

    today = date.today().isoformat()
    changed = False
    if state["last_date"] is None:
        # First-ever run: start at day 1 without incrementing.
        state["current_day"] = 1
        state["last_date"] = today
        changed = True
    elif today != state["last_date"]:
        state["current_day"] = min(state["current_day"] + 1, total)
        state["last_date"] = today
        changed = True

    day = state["current_day"]
    entry = days.get(day)
    if entry is None:
        print(f"Day {day} not in schedule (total {total}) — stopping.")
        if changed:
            json.dump(state, open(STATE_FILE, "w"), indent=2)
        return

    # ---- build issue body ----
    b = entry["body"]
    lines = [f"## {entry['week']}", f"**Topic:** {b['topic']}", ""]
    lines.append("### Tasks")
    for i, t in enumerate(b["tasks"], 1):
        lines.append(f"- [ ] {t}")
    if b.get("resources"):
        lines.append("")
        lines.append("### Resources")
        for u in b["resources"]:
            lines.append(f"- {u}")
    lines.append("")
    lines.append("---")
    lines.append("**Logbook rule:** work through the tasks, tick them, and reply with a 3-line"
                 " note on what you learned. Complete issues are proof for GitHub." )
    body = "\n".join(lines)

    title = entry["title"]
    labels = ["daily-study", f"day-{day}"]

    # ---- ensure today's issue exists ----
    existing = gh_call("issue", "list", "--state", "all",
                       "--search", f'label:"day-{day}"', "--json", "number", "--limit", "1")
    issue_number = None
    if existing and existing != "[]":
        issue_number = json.loads(existing)[0]["number"] if not DRY else day
    if issue_number is None:
        out = gh_call("issue", "create", "--title", title, "--body", body,
                      "--label", ",".join(labels))
        print(f"Created issue for day {day}: {out}")
    else:
        print(f"Day {day} issue #{issue_number} already exists — leaving it.")

    # ---- close stale open daily-study issues from earlier days ----
    open_issues = gh_call("issue", "list", "--state", "open",
                          "--label", "daily-study", "--json", "number,labels")
    if open_issues and open_issues != "[]":
        for i in json.loads(open_issues):
            lbls = {l.get("name") for l in i.get("labels", [])}
            this_day = f"day-{day}" in lbls
            if not this_day:
                gh_call("issue", "close", str(i["number"]),
                        "--comment", f"Auto-closed: day {day} is the active study day.")

    # ---- persist state ----
    if changed and not DRY:
        json.dump(state, open(STATE_FILE, "w"), indent=2)
        run("git", "add", ".study-progress.json", cwd=REPO)
        run("git", "-c", "user.name=StudyBot", "-c", "user.email=studybot@users.noreply.github.com",
            "commit", "-m", f"advance study day to {day}", cwd=REPO)
        run("git", "push", cwd=REPO)
    print(f"State: current_day={state['current_day']}, last_date={state['last_date']}")

if __name__ == "__main__":
    main()