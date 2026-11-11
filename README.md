<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="0HBrar0 — systems, automation, experiments. A signal line branching into three projects: tell-my-pc, world-line and watcher-simulator." src="assets/header-dark.svg" width="100%">
</picture>

I like finding out how systems actually work, then building something small and real on top of them. Lately that means AI agents that run safely on my own machine, browser apps that explain complicated things, and anything that connects software to the physical world.

Computer Systems Technician graduate from Humber Polytechnic, working toward cloud infrastructure, security and systems roles.

<br>

## Selected work

### [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp;·&nbsp; <sub>Python · v1.3.0</sub>

Say *"Hey Siri, Tell Claude"*, dictate a task, put the phone away. A self-hosted daemon runs it with Claude Code on its own git branch and pushes a short report back to the phone.

The interesting part is containment: every tool call passes through a hook that enforces permission tiers (read, work, ask-on-phone, never), credential files and system folders are off-limits, and the list of changed files comes from `git diff`, not from the model. Design choices are written up as decision records alongside a threat model.

`Python 3.12` `Starlette` `Tailscale` `ntfy` `pytest` · [docs](https://0hbrar0.github.io/tell-my-pc/) · [threat model](https://github.com/0HBrar0/tell-my-pc/blob/main/docs/threat-model.md)

### [world-line](https://github.com/0HBrar0/world-line) &nbsp;·&nbsp; <sub>TypeScript · live</sub>

<a href="https://0hbrar0.github.io/world-line/"><img src="assets/world-line.png" alt="World Line home page: the headline 'One text message to the past can rewrite history' over glowing branching lines." width="100%"></a>

An interactive, spoiler-safe explainer of the *Steins;Gate* time-travel story: a branching world-line map, animated mechanic walkthroughs, and a guided story mode. Every story fact comes from one validated data file and shows a confidence badge linking to its sources, and spoiler tiers keep later content out of the page entirely until you unlock it.

`React` `TypeScript` `Zod` `Framer Motion` `Vitest` `Playwright` · [open the site →](https://0hbrar0.github.io/world-line/)

### [watcher-simulator](https://github.com/0HBrar0/watcher-simulator) &nbsp;·&nbsp; <sub>TypeScript · live</sub>

A 3D universe you can fly through in the browser, then watch through the eyes of the cosmic observer who has been looking at it all along. Zoom far enough into Earth and it hands off to real satellite imagery and street maps, lined up with the 3D planet. Unofficial fan project.

`Three.js` `React Three Fiber` `MapLibre GL` `WebGL 2` `GitHub Actions` · [open the site →](https://0hbrar0.github.io/watcher-simulator/)

<br>

## On the bench

Not public yet, so treat these as directions rather than results.

- **Audiolocate** — can a sound recording be placed on a map from acoustic evidence alone? Signal processing, physical models and reference data.
- **Bioverse** — an early concept for an explorable biological atlas with 3D anatomy and cited sources.

<br>

## Telemetry

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/telemetry-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/telemetry-light.svg">
  <img alt="Live telemetry for my public projects: number of projects, commits over the last 12 weeks, language mix, and weekly commit activity per project." src="assets/telemetry-dark.svg" width="100%">
</picture>

<sub>LATEST COMMITS</sub><br>
<!-- log:start -->
`2026-11-11` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Redraw the mechanic animations as ink diagrams](https://github.com/0HBrar0/world-line/commit/99eed8280a91b529f7b0a98417643db0b753f561)<br>
`2026-11-10` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Read a D-Mail on a phone without leaving the page](https://github.com/0HBrar0/world-line/commit/8d471ba659b657a83a0fb0cba9be9151bd402426)<br>
`2026-11-10` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Rope map, clockwork motion and a Sources switch](https://github.com/0HBrar0/world-line/commit/eea16b82ba3f02686c07d3799f31cd3b3a97375f)<br>
`2026-11-10` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Drop the grain and gear layers on the chart page](https://github.com/0HBrar0/world-line/commit/d27a878e37b6aeb9c4661b2cc9423db3554bdb94)<br>
`2026-11-10` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Keep the gears still behind the map so panning stays smooth](https://github.com/0HBrar0/world-line/commit/0dc847603ccf0fd079e24f4c70aa949d598ee955)<br>
`2026-11-10` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Release 3.0.0: paper-and-gears redesign, the chronicle and D-Mail wording](https://github.com/0HBrar0/world-line/commit/5a1b0dfe926ea247db4e7d1b068500f6ca2755cc)<br>
<!-- log:end -->

<sub>This section rebuilds itself every day: a [GitHub Action](.github/workflows/build.yml) runs a [small Python script](scripts/build.py) against the GitHub API and redraws the panel. No third-party widgets.</sub>

<br>

## Toolkit

**Use regularly** — Python · TypeScript / React · Git & GitHub Actions · Linux & the command line · Windows & PowerShell<br>
**Solid on the fundamentals** — Networking · SQL & databases · AWS · security fundamentals<br>
**Learning now** — Cloud infrastructure, DevOps & SRE · operating systems · AI agent tooling · algorithms

## Credentials

- **Humber Polytechnic** — Computer Systems Technician
- **AWS** Certified Cloud Practitioner
- **ISC2** Certified in Cybersecurity (CC)

<br>

<sub>Reach me here on GitHub: opening an issue on any repo is the best way.</sub>

<!--
  Contact links: add yours on the line above when ready, e.g.
  <a href="https://www.linkedin.com/in/YOUR-HANDLE/">LinkedIn</a>
-->
