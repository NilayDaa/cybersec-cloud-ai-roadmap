#!/usr/bin/env python3
"""One-time: pre-create ALL 72 study issues on GitHub (idempotent)."""
import json, os, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHED = os.path.join(REPO, "schedule.json")
GH = "gh"
DRY = "--dry-run" in sys.argv

def gh_call(*args):
    if DRY:
        print("DRY: gh", " ".join(str(a) for a in args)); return "[]"
    r = subprocess.run([GH, *[str(a) for a in args]], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {(r.stderr or r.stdout).strip()}")
    return r.stdout.strip()

def ensure_label(label, color="1d76db"):
    # --force makes creation idempotent (updates if exists).
    gh_call("label", "create", label, "--color", color,
            "--description", f"Study tracker label: {label}", "--force")
    print(f"label ok: {label}")

def main():
    sched = json.load(open(SCHED))
    total = sched["total_days"]
    ensure_label("daily-study")
    created = existing = 0
    for d in sched["days"]:
        day = d["day"]
        ensure_label(f"day-{day}", "5319e7")
        b = d["body"]
        lines = [f"## {d['week']}", f"**Topic:** {b['topic']}", ""]
        lines.append("### Tasks")
        for i, t in enumerate(b["tasks"], 1):
            lines.append(f"- [ ] {t}")
        if b.get("resources"):
            lines.append(""); lines.append("### Resources")
            for u in b["resources"]:
                lines.append(f"- {u}")
        lines.append("")
        lines.append("---")
        lines.append("**Logbook rule:** work through the tasks, tick them, and reply with a 3-line"
                     " note on what you learned. Complete issues are proof for GitHub.")
        body = "\n".join(lines)
        found = gh_call("issue", "list", "--state", "all",
                        "--search", f'label:"day-{day}"', "--json", "number", "--limit", "1")
        if found and found != "[]":
            existing += 1
            print(f"[{existing}] day {day} exists — skip")
            continue
        out = gh_call("issue", "create", "--title", d["title"], "--body", body,
                      "--label", "daily-study," + f"day-{day}")
        created += 1
        print(f"[+{created}] created day {day}: {out}")
    print(f"DONE. created={created}, already_exists={existing}, total={total}")

if __name__ == "__main__":
    main()