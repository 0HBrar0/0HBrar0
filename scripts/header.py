"""Draw the profile header (assets/header-dark.svg, assets/header-light.svg). Run: python scripts/header.py"""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
THEMES = {
 "dark":  dict(bg="#0d1117", border="#1c2a2b", grid="#16212a", text="#e6edf3", muted="#7d8b93", accent="#3fd0b0", accent2="#2a8f80", dim="#22333a"),
 "light": dict(bg="#ffffff", border="#d0d7de", grid="#eef2f4", text="#1f2328", muted="#59636e", accent="#0f8a74", accent2="#5fb3a3", dim="#d5e2e0"),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
def svg(t):
    c = THEMES[t]
    grid = "".join(f'<line x1="{x}" y1="24" x2="{x}" y2="296" stroke="{c["grid"]}" stroke-width="1"/>' for x in range(80, 1200, 80))
    ticks = "".join(f'<line x1="{x}" y1="246" x2="{x}" y2="{252 if x%160 else 256}" stroke="{c["muted"]}" stroke-opacity=".5" stroke-width="1"/>' for x in range(64, 680, 32))
    branches = [(120, "tell-my-pc"), (185, "world-line"), (250, "watcher-simulator")]
    paths, nodes, pulses = "", "", ""
    for i,(y,label) in enumerate(branches):
        paths += f'<path d="M680 250 C 790 250, 820 {y}, 930 {y} L 1100 {y}" fill="none" stroke="{c["accent"] if i==0 else c["accent2"]}" stroke-width="{1.6 if i==0 else 1.2}" stroke-opacity="{1 if i==0 else .8}"/>'
        route = f"M40 250 L680 250 C 790 250, 820 {y}, 930 {y} L 1100 {y}"
        pulses += (f'<circle class="pulse" r="2.6" fill="{c["accent"]}" opacity="0">'
                   f'<animateMotion dur="7s" begin="{i * 2.3}s" repeatCount="indefinite" path="{route}"/>'
                   f'<animate attributeName="opacity" dur="7s" begin="{i * 2.3}s" repeatCount="indefinite" '
                   f'values="0;.9;.9;0" keyTimes="0;.08;.85;1"/></circle>')
        nodes += (f'<circle cx="1100" cy="{y}" r="4" fill="{c["bg"]}" stroke="{c["accent"]}" stroke-width="1.5"/>'
                  f'<text x="1088" y="{y-10}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{label}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-labelledby="t d">
<title id="t">0HBrar0</title>
<desc id="d">Header: the handle 0HBrar0 over a signal line that branches into three public projects.</desc>
<style>@keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}.p{{animation:p 2.4s ease-in-out infinite}}@media (prefers-reduced-motion:reduce){{.p{{animation:none}}.pulse{{display:none}}}}</style>
<rect x="0.5" y="0.5" width="1199" height="319" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>
<g>{grid}</g>
<text x="64" y="64" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{c["muted"]}">~/whoami</text>
<circle class="p" cx="1101" cy="59" r="3.5" fill="{c["accent"]}"/>
<text x="1088" y="64" text-anchor="end" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{c["muted"]}">building</text>
<text x="62" y="140" font-family="{SANS}" font-size="58" font-weight="600" letter-spacing="-0.5" fill="{c["text"]}">0HBrar0</text>
<text x="64" y="182" font-family="{MONO}" font-size="17" fill="{c["accent"]}">systems · automation · experiments</text>
<line x1="40" y1="250" x2="680" y2="250" stroke="{c["accent"]}" stroke-width="1.6"/>
<g>{ticks}</g>
<text x="64" y="280" font-family="{MONO}" font-size="12" fill="{c["muted"]}">t = 0 · Canada</text>
<g>{paths}</g><g>{nodes}</g>
<circle cx="680" cy="250" r="5" fill="{c["accent"]}"/>
{pulses}
</svg>'''
for t in THEMES: (OUT / f"header-{t}.svg").open("w").write(svg(t))
