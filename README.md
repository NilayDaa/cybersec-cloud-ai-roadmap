# 🔐 Cybersec + Cloud + AI — 12-Week Sprint

Compressed full-time study roadmap (Cybersecurity · SOC · Cloud/Azure · DevSecOps · AI/LLM · AI Security) for a JAMK cybersecurity student targeting Finland internships. **~6 study days/week, 8h/day.**

This repo auto-creates one focused issue per day via GitHub Actions so you always know exactly what to study.

## How it works
- `docs/ROADMAP.md` — the full 12-week plan with every resource linked inline
- `docs/resources.md` — searchable catalog of ALL verified resource links by topic
- `schedule.json` — generated daily task plan (machine-readable)
- `.github/workflows/daily-issue.yml` — nightly job that opens the next day's issue with `daily-study` label, then closes the previous day's

## Daily loop
1. GitHub Actions opens **today's issue** at 07:00 UTC (10:00 Finland) with the exact tasks + resources
2. Study, tick the checkboxes, add a 2-line logbook note as a comment
3. Your daily commit/reply = proof of progress on GitHub
4. Next run closes the finished issue and opens the new one

## Fast start
```bash
# install git, then clone your fork
git clone <your-fork-url>
# next day's issue appears automatically — no setup
```

## Status
Track overall progress in the Issues tab (one issue = one study day).