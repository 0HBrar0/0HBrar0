#!/usr/bin/env python3
"""Rebuild the dynamic parts of the profile README.

Pulls public data for the account from the GitHub API, then:
  * draws assets/telemetry-dark.svg and assets/telemetry-light.svg
  * rewrites the block between <!-- log:start --> and <!-- log:end --> in README.md

Standard library only. Run in GitHub Actions with GITHUB_TOKEN set, or locally:
    python scripts/build.py                     # live API (needs GITHUB_TOKEN)
    python scripts/build.py --fixture data.json # offline, from a saved snapshot
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import urllib.request
from pathlib import Path

USER = "0HBrar0"
ROOT = Path(__file__).resolve().parent.parent
WEEKS = 12
LOG_ITEMS = 6

THEMES = {
    "dark": dict(bg="#0d1117", border="#1c2a2b", grid="#16212a", text="#e6edf3", muted="#7d8b93",
                 accent="#3fd0b0", track="#16232a",
                 langs=["#3fd0b0", "#2a8f80", "#7fb8ad", "#4d6b73", "#33464d", "#25343a"]),
    "light": dict(bg="#ffffff", border="#d0d7de", grid="#eef2f4", text="#1f2328", muted="#59636e",
                  accent="#0f8a74", track="#e6eeed",
                  langs=["#0f8a74", "#4fa695", "#8cc7bb", "#6e8a91", "#a9bcc0", "#cfdcde"]),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


# ---------------------------------------------------------------- data

def api(path: str):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-build",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch() -> dict:
    """Snapshot of public, non-fork, non-archived repos (excluding this profile repo)."""
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(weeks=WEEKS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    repos = []
    for r in api(f"/users/{USER}/repos?type=owner&per_page=100"):
        if r["fork"] or r["archived"] or r["private"] or r["name"].lower() == USER.lower():
            continue
        commits, page = [], 1
        while True:
            batch = api(f"/repos/{USER}/{r['name']}/commits?per_page=100&page={page}")
            commits += [{"sha": c["sha"], "date": c["commit"]["committer"]["date"],
                         "message": c["commit"]["message"].splitlines()[0], "url": c["html_url"]} for c in batch]
            if len(batch) < 100 or page >= 10:
                break
            page += 1
        repos.append({"name": r["name"], "url": r["html_url"], "pushed_at": r["pushed_at"],
                      "languages": api(f"/repos/{USER}/{r['name']}/languages"), "commits": commits})
    return {"generated": dt.datetime.now(dt.timezone.utc).isoformat(), "since": since, "repos": repos}


# ---------------------------------------------------------------- helpers

def parse(ts: str) -> dt.datetime:
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def short_date(d: dt.datetime) -> str:
    return f"{d:%b} {d.day}"


def weekly(commits, now):
    buckets = [0] * WEEKS
    for c in commits:
        age = (now - parse(c["date"])).days // 7
        if 0 <= age < WEEKS:
            buckets[WEEKS - 1 - age] += 1
    return buckets


# ---------------------------------------------------------------- telemetry svg

def telemetry(data: dict, theme: str) -> str:
    c = THEMES[theme]
    now = parse(data["generated"])
    repos = sorted(data["repos"], key=lambda r: max((x["date"] for x in r["commits"]), default=""), reverse=True)

    langs: dict[str, int] = {}
    for r in repos:
        for k, v in r["languages"].items():
            langs[k] = langs.get(k, 0) + v
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: kv[1], reverse=True)
    if len(top) > 5:
        top = top[:5] + [("Other", sum(v for _, v in top[5:]))]

    recent = sum(sum(weekly(r["commits"], now)) for r in repos)
    rows_y0, row_h = 196, 40
    H = rows_y0 + row_h * len(repos) + 34

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {H}" width="1200" height="{H}" role="img" aria-labelledby="t d">',
           f'<title id="t">Telemetry for {USER}</title>',
           f'<desc id="d">{len(repos)} public projects, {recent} commits in the last {WEEKS} weeks. Languages: '
           + esc(", ".join(f"{k} {v / total:.0%}" for k, v in top)) + ".</desc>",
           f'<rect x="0.5" y="0.5" width="1199" height="{H - 1}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>',
           f'<text x="64" y="52" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{c["muted"]}">telemetry</text>',
           f'<text x="1136" y="52" text-anchor="end" font-family="{MONO}" font-size="13" letter-spacing="1" fill="{c["muted"]}">rebuilt {short_date(now)}, {now.year}</text>']

    # headline numbers
    for i, (val, label) in enumerate([(len(repos), "public projects"), (recent, f"commits · {WEEKS} wks"), (len(langs), "languages")]):
        x = 64 + i * 150
        out.append(f'<text x="{x}" y="118" font-family="{SANS}" font-size="38" font-weight="600" fill="{c["text"]}">{val}</text>')
        out.append(f'<text x="{x + 1}" y="142" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{esc(label)}</text>')

    # language bar
    bx, bw = 560, 576
    out.append(f'<rect x="{bx}" y="84" width="{bw}" height="8" rx="4" fill="{c["track"]}"/>')
    out.append(f'<clipPath id="bar"><rect x="{bx}" y="84" width="{bw}" height="8" rx="4"/></clipPath><g clip-path="url(#bar)">')
    x = bx
    for i, (name, v) in enumerate(top):
        w = bw * v / total
        out.append(f'<rect x="{x:.1f}" y="84" width="{max(w - 2, 1):.1f}" height="8" fill="{c["langs"][i]}"/>')
        x += w
    out.append("</g>")
    for i, (name, v) in enumerate(top):
        lx, ly = bx + (i % 3) * 196, 122 + (i // 3) * 24
        out.append(f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4" fill="{c["langs"][i]}"/>')
        out.append(f'<text x="{lx + 16}" y="{ly}" font-family="{MONO}" font-size="12" fill="{c["text"]}">{esc(name)} '
                   f'<tspan fill="{c["muted"]}">{v / total:.1%}</tspan></text>')

    # per-project rows
    out.append(f'<line x1="64" y1="{rows_y0 - 22}" x2="1136" y2="{rows_y0 - 22}" stroke="{c["grid"]}"/>')
    for i, r in enumerate(repos):
        y = rows_y0 + i * row_h + 12
        weeks = weekly(r["commits"], now)
        last = max((parse(x["date"]) for x in r["commits"]), default=parse(r["pushed_at"]))
        active = (now - last).days <= 30
        dot = c["accent"] if active else c["muted"]
        out.append(f'<circle cx="68" cy="{y - 4}" r="3.5" fill="{dot}" fill-opacity="{1 if active else 0.5}"/>')
        out.append(f'<text x="84" y="{y}" font-family="{MONO}" font-size="14" fill="{c["text"]}">{esc(r["name"])}</text>')
        peak = max(weeks) or 1
        for j, n in enumerate(weeks):
            h = 2 if n == 0 else 4 + 18 * n / peak
            out.append(f'<rect x="{430 + j * 22}" y="{y + 2 - h:.1f}" width="14" height="{h:.1f}" rx="2" '
                       f'fill="{c["accent"] if n else c["track"]}" fill-opacity="{1 if n else 1}"/>')
        out.append(f'<text x="{720}" y="{y}" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{len(r["commits"])} commits</text>')
        out.append(f'<text x="1136" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["muted"]}">'
                   f'{"active" if active else "quiet"} · last commit {short_date(last)}</text>')
    out.append(f'<text x="430" y="{H - 16}" font-family="{MONO}" font-size="11" fill="{c["muted"]}">← {WEEKS} weeks of commits, one bar per week</text>')
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- readme log

def commit_log(data: dict) -> str:
    items = [(parse(c["date"]), r["name"], r["url"], c) for r in data["repos"] for c in r["commits"]]
    items.sort(key=lambda t: t[0], reverse=True)
    lines = []
    for d, name, url, c in items[:LOG_ITEMS]:
        msg = c["message"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
        lines.append(f"`{d:%Y-%m-%d}` &nbsp; [{name}]({url}) &nbsp; [{msg}]({c['url']})<br>")
    return "\n".join(lines)


def rewrite_readme(block: str) -> None:
    p = ROOT / "README.md"
    text = p.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- log:start -->).*?(<!-- log:end -->)",
                 lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", text, flags=re.S)
    if new != text:
        p.write_text(new, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", help="read data from this JSON file instead of the API")
    ap.add_argument("--save", help="also save the fetched data to this JSON file")
    a = ap.parse_args()
    data = json.loads(Path(a.fixture).read_text()) if a.fixture else fetch()
    if a.save:
        Path(a.save).write_text(json.dumps(data, indent=1))
    for t in THEMES:
        (ROOT / "assets" / f"telemetry-{t}.svg").write_text(telemetry(data, t), encoding="utf-8")
    rewrite_readme(commit_log(data))
    print(f"built: {len(data['repos'])} repos, generated {data['generated']}")


if __name__ == "__main__":
    main()
