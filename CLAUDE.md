# FretPath

## System Map — Read First

Before substantive work in this repo, read **`~/.claude/System Map.md`**. It documents Adam's cross-project information architecture: repo vs vault placement, folder conventions, and cross-reference patterns. FretPath is a Tier 1 product repo. Its Tier 2 docs (product brief, roadmap, decisions) belong in the Development vault under `PRODUCTS/APPLICATIONS/FRETPATH/`. That folder does not exist yet; create it when the first product-level doc is needed.

## Overview

A knowledge-based agent that picks guitar fingerings for a whole chord progression. Given a progression, it generates playable voicings for each chord, scores each change using ergonomic and voice-leading knowledge, searches for the easiest sequence, and explains its choices.

This is a learning project. Adam is a guitar beginner with a piano background, building this to practice the techniques from Georgia Tech CS 7637 (Knowledge-Based AI) and to actually use while playing.

## Tech Stack

- **Python 3.13+**, standard library only for now. NumPy is acceptable if needed.
- `src/` layout. Package: `src/fretpath/`.
- Tests: `unittest`, in `tests/`.

## Documentation Index (in this repo)

| Document | Path | Purpose |
|----------|------|---------|
| Architecture | `Documentation/Architecture.md` | Agent pipeline and which KBAI technique each stage uses |
| Claude Lessons | `Claude/Claude-Lessons.md` | Project-specific lessons (create when first needed) |

## External Documentation (outside this repo)

- **Development vault, product docs:** `~/Developer/Obsidian-Notes/Development/PRODUCTS/APPLICATIONS/FRETPATH/` (not yet created)
- **KBAI course notes:** `~/Developer/Obsidian-Notes/Development/KNOWLEDGE/Computer Science/Knowledge-Based AI/Lesson Notes/`. Use these to match the course's terminology and framing of each technique.

## When to Reference What

- **Designing or changing an agent stage:** read `Documentation/Architecture.md`, then the matching lesson note in the KBAI course folder.
- **Product scope or priorities:** the Development vault folder above, once it exists.

## Commands

- `pip install -e .`: install in editable mode (inside `.venv`)
- `python -m unittest discover tests`: run tests

## Conventions

**This is a learning project. Adam writes the agent logic himself.**
- Act as a tutor and reviewer. Explain concepts, review his code, point out bugs, and suggest approaches. Do not write the knowledge representation, rules, or search code for him unless he explicitly asks for it in that moment.
- Scaffolding, tooling, tests he asks for, and docs are fine to write directly.

**Academic integrity (CS 7637):**
- Never copy code from Adam's graded course submissions (`~/Developer/CS7637-KBAI/`: Sheep & Wolves, Block World, Sentence Reading, ARC-AGI, game agents) into this repo. This repo is public, and the course prohibits posting submitted work publicly. Reimplementing the ideas from scratch is fine.
- Never move work the other way either. Nothing from this repo goes into a course deliverable.

**Lessons capture:** when a correction or non-obvious fix comes up, decide whether it is project-specific or reusable (see the Self-Improvement Loop in the global `~/.claude/CLAUDE.md`):
- **Project-specific** → append to `Claude/Claude-Lessons.md`.
- **Reusable** (Python, search, or general music-theory knowledge) → propose a destination and ask before writing.
- **When in doubt, ask.**

**Prohibited Changes:**
- Do not stage, add, or commit without explicit permission.
