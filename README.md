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
`2026-11-08` &nbsp; [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp; [feat: local dashboard](https://github.com/0HBrar0/tell-my-pc/commit/a172c43f04d477596616b6a55ba2a1f557004cb0)<br>
`2026-11-08` &nbsp; [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp; [feat: tasks on the computer itself](https://github.com/0HBrar0/tell-my-pc/commit/fcd7212354270ee8975beb7609fe713a990992c1)<br>
`2026-11-08` &nbsp; [world-line](https://github.com/0HBrar0/world-line) &nbsp; [Release 2.0.0: lab-bench redesign, world-line tracker and D-Mail files](https://github.com/0HBrar0/world-line/commit/85464fe14b13e58cae20330ab2310e4e25386d61)<br>
`2026-11-08` &nbsp; [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp; [feat: autostart on macOS and Linux; serve waits for Tailscale](https://github.com/0HBrar0/tell-my-pc/commit/5d311164469ce484e65c4975c71c26fe0f39cfa9)<br>
`2026-11-07` &nbsp; [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp; [docs: changelog and release notes for 1.0.0](https://github.com/0HBrar0/tell-my-pc/commit/4c461da26cd1ef6b913ccaeb435402eba0c03c86)<br>
`2026-11-07` &nbsp; [tell-my-pc](https://github.com/0HBrar0/tell-my-pc) &nbsp; [docs: GitHub Pages site from docs/](https://github.com/0HBrar0/tell-my-pc/commit/76c0297efeeede2da911479ba7f8dc475a4ed614)<br>
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
