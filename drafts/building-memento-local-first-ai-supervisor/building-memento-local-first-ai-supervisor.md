# Building Memento: A Local-First AI Supervisor for Your Life

**Published:** April 2026
**Categories:** AI, Software
**Tags:** ai, memento, local-first, python, personal-assistant
**LinkedIn:** YES

---

**Copyright © 2026 Ivan Judson. All Rights Reserved.**

## SEO Metadata
- **SEO Title:** Building Memento: A Local-First AI Supervisor
- **Meta Description:** How I built a personal AI daemon that watches my work, reflects on what I'm doing, and helps me stay intentional — without sending my data to the cloud.
- **URL Slug:** building-memento-local-first-ai-supervisor

---

Most AI tools are designed to respond. You ask, they answer. What I wanted was something different — a system that *watches*, *thinks*, and occasionally *interrupts* me with something useful. Not a chatbot. A supervisor. I called it Memento.

---

## Why I Built It

I've spent a long time working at the intersection of AI and systems software. One thing I've learned: the gap between "AI can do this" and "AI is actually helping me do this reliably" is enormous, and almost nobody talks honestly about what it takes to close it.

I kept noticing that my own work life had a pattern problem. I'd spend a week heads-down on something, surface for air, and realize I'd drifted from what actually mattered. Not because I was lazy — because the work itself pulls you along. Code begets code. Meetings beget meetings. Without something actively watching the bigger picture, it's easy to be productive and off-course at the same time.

I didn't want another SaaS dashboard. I didn't want my work data leaving my machine. I wanted a daemon — something running locally, continuously, with access to what I'm actually doing — that could reflect back a useful signal about whether I was spending my time well.

That's Memento.

---

## What Memento Does

At its core, Memento is a Python service that runs on my local machine and acts as a supervisor layer over my digital work life. It has a few key behaviors:

**It watches.** Memento monitors my active projects, git activity, file changes, and system state. It doesn't screen-record me or log keystrokes — it tracks meaningful signals. Which repos am I committing to? What's the cadence? What tools am I running? What's sitting idle that shouldn't be?

**It reflects.** On a configurable schedule — I run it a few times a day — Memento compiles a summary of what it's observed and runs it through a local LLM. The prompt is tuned to look for drift, idle threads, and anything that looks like it needs attention. The output is a short, plain-text brief. No charts, no dashboards. Just a few sentences I can read in thirty seconds.

**It remembers.** This is the part that makes the name fit. Memento keeps a rolling log of its observations and reflections. Over time, that log becomes a kind of externalized working memory — a record of what I was doing and what I thought about it. It's searchable. It's local. It's mine.

---

## The Architecture

The technical design was driven by one constraint: everything runs on my hardware, and nothing leaves unless I explicitly send it somewhere.

Memento is built in Python. The core loop is a lightweight scheduler that fires observation tasks, aggregates results into a context packet, and hands that packet to an LLM for reflection. I'm running a local model via [Ollama](https://ollama.com/) — right now a mid-size Mistral variant that's fast enough to not feel like waiting, and capable enough to produce useful output.

The observation layer is modular. Each "sensor" is a small Python class that implements a simple interface: `observe()` returns structured data, and `describe()` returns a human-readable label for logging. Current sensors include:

- **Git sensor:** recent commits, active branches, stale branches, repos with uncommitted work
- **File system sensor:** recently modified files, large file changes, new files in watched directories
- **Process sensor:** long-running processes, resource hogs, services that should or shouldn't be running
- **Docker sensor:** container states, volume usage, services that have been up (or down) unexpectedly long

Each sensor is intentionally narrow. The goal isn't omniscience — it's a curated signal that an LLM can reason about without drowning in noise.

The reflection layer takes the aggregated sensor output, formats it into a structured prompt, and asks the model a small set of questions: What's notable here? What looks like drift from stated priorities? What deserves attention today? The model's response gets logged, optionally summarized further, and surfaced to me as a notification or written to a daily brief file I check in the morning.

MCP (Model Context Protocol) tools are how Memento interacts with the rest of my environment — it can query system state, inspect Docker containers, read files, and run git commands through a clean interface that keeps the system composable and testable.

---

## What I Learned Building It

A few things surprised me.

**The value isn't in the AI — it's in the observation discipline.** Building the sensors forced me to think precisely about what "meaningful work signal" actually means. What does a healthy week of git activity look like versus a scattered one? What file change patterns indicate real progress versus churn? Just answering those questions was clarifying, before the LLM touched a single token.

**Local models are good enough for this use case.** I was skeptical, but a 7B-parameter model running locally handles summarization and reflection tasks competently. The prompts are tight, the context is structured, and "good enough" genuinely is good enough when you're asking for a brief, not a dissertation. The privacy and latency benefits are real.

**Reflection cadence matters more than reflection depth.** I experimented with long, detailed prompts that asked the model to produce elaborate analyses. They were impressive and useless. The most valuable output is three sentences I'll actually read at 8am. Short, specific, actionable beats thorough every time.

**The memory layer is underrated.** Having a searchable log of past reflections turns out to be genuinely useful in ways I didn't anticipate. When I'm trying to remember why I made a decision, or reconstruct what was happening during a particular week, the log is there. It's not a replacement for good notes — it's a complement to them.

---

## What's Next

Memento is a working tool, not a finished product. A few things I'm actively developing:

- **Priority integration:** Right now Memento observes what I'm doing, not what I said I *would* do. I'm wiring in a simple priority file — a plain-text list of current commitments — so the reflection layer can compare stated priorities against observed behavior. That delta is where the real value is.

- **Weekly synthesis:** Daily briefs are useful, but a weekly synthesis that looks across the whole week's log and surfaces patterns is on the roadmap. Something like a retrospective that I didn't have to run myself.

- **Extensible sensors:** I want to make it easier to add new sensors without touching the core loop. The current sensor interface is clean but the wiring is still a bit manual. A proper plugin system would let this grow without becoming a mess.

- **Open source:** I'm planning to release the core of Memento publicly. The sensor framework and reflection loop are general enough to be useful to others. The specific sensors I'm running are idiosyncratic, but the scaffolding isn't.

---

## Conclusion

I built Memento because I wanted to stay intentional about how I spend my time, and I didn't trust myself to do it manually. The best systems are the ones that encode the behavior you want to have, and then run quietly in the background making it easier to have it.

What I've found after running Memento for a few months is that the value isn't magic — it's consistency. The model doesn't tell me anything I couldn't figure out myself with enough reflection. But it reflects on my behalf, every day, without me having to remember to do it. That's worth a lot.

If you're building something similar, or thinking about how to add meaningful AI supervision to your own workflow without surrendering your data to a third party, I'd like to compare notes. Reach out through the contact page or find me on LinkedIn.

---

# LINKEDIN VERSION

I got tired of being productive and off-course at the same time. So I built a local AI daemon to watch my work and tell me when I'm drifting.

→ **𝗪𝗵𝗮𝘁 𝗶𝘁 𝗱𝗼𝗲𝘀:** Monitors git activity, file changes, running processes, and Docker state — then runs local LLM reflection on the signal a few times a day
→ **𝗪𝗵𝘆 𝗹𝗼𝗰𝗮𝗹:** Nothing leaves my machine. A 7B-parameter model running via Ollama handles summarization and reflection competently — and the privacy + latency wins are real
→ **𝗕𝗶𝗴𝗴𝗲𝘀𝘁 𝗹𝗲𝘀𝘀𝗼𝗻:** The value isn't the AI — it's the observation discipline. Building the sensors forced me to define precisely what "meaningful work signal" actually means
→ **𝗪𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝘄𝗼𝗿𝗸𝘀:** Three sentences I'll read at 8am beats a thorough analysis I won't. Reflection cadence matters more than reflection depth

The best systems encode the behavior you want to have, then run quietly in the background making it easier to have it.

Full writeup on the architecture, what surprised me, and what's next → [BLOG_URL]

#AIEngineering #LocalFirst #PersonalAI #BuildingWithAI #Python