# AI Agent Instructions

This project uses the global AI operating system at the user-level global source for this machine:

```txt
macOS: /Users/jamestylee/.ai
Windows: %USERPROFILE%\.ai
```

This same content may be copied into tool-specific instruction files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CURSOR.md`, `WINDSURF.md`, `.github/copilot-instructions.md`, or another instruction filename used by a coding assistant.

The global AI source contains reusable agents, skills, rules, workflows, and templates. Do not copy those global assets into this project unless a project-specific override is explicitly needed.

---

## Source Of Truth

For this project, the source of truth is:

- the files in this repository
- this repository's `MEMORY.md`
- this repository's `CHANGELOG_AI.md`

Do not rely on prior chat history as the source of truth.

Use the global repository for reusable operating rules and agent definitions:

- macOS: `/Users/jamestylee/.ai/AGENTS.md`; Windows: `%USERPROFILE%\.ai\AGENTS.md`
- macOS: `/Users/jamestylee/.ai/.ai/agents/`; Windows: `%USERPROFILE%\.ai\.ai\agents\`
- macOS: `/Users/jamestylee/.ai/.ai/skills/`; Windows: `%USERPROFILE%\.ai\.ai\skills\`
- macOS: `/Users/jamestylee/.ai/.ai/rules/`; Windows: `%USERPROFILE%\.ai\.ai\rules\`
- macOS: `/Users/jamestylee/.ai/.ai/workflows/`; Windows: `%USERPROFILE%\.ai\.ai\workflows\`
- macOS: `/Users/jamestylee/.ai/.ai/templates/`; Windows: `%USERPROFILE%\.ai\.ai\templates\`

Do not treat `/Users/jamestylee/.ai/CHANGELOG_AI.md` as this project's handoff ledger. Use this project's local `CHANGELOG_AI.md`.

---

## Required Startup

Before editing code or project files:

1. Read the global `AGENTS.md` for this machine: `/Users/jamestylee/.ai/AGENTS.md` on macOS or `%USERPROFILE%\.ai\AGENTS.md` on Windows.
2. Read this project's `MEMORY.md`. If it does not exist, create it from the starter below.
3. Read this project's `CHANGELOG_AI.md`. If it does not exist, create it from the starter below.
4. Read the global `agent-team-selection.md` rule from `/Users/jamestylee/.ai/.ai/rules/` on macOS or `%USERPROFILE%\.ai\.ai\rules\` on Windows.
5. Read the global `ai-handoff.md` rule from `/Users/jamestylee/.ai/.ai/rules/` on macOS or `%USERPROFILE%\.ai\.ai\rules\` on Windows.
6. Inspect the repository if the latest handoff appears stale, incomplete, or inconsistent.
7. Read only the global agent profiles needed for the current task.
8. Select the smallest useful team of agents.
9. State the selected team before implementation.
10. Check repository status before making edits.

Do not load every global agent by default.

---

## Agent, Skill, And Rule Model

- Agents answer: who is doing the work.
- Skills answer: how the work is performed.
- Rules answer: what must never be violated.

Use global agents, skills, and rules from `/Users/jamestylee/.ai/.ai/` on macOS or `%USERPROFILE%\.ai\.ai\` on Windows.

Create project-local agent, skill, or rule files only when the instruction is genuinely specific to this repository.

---

## Local MEMORY.md Starter

If `MEMORY.md` does not exist in this project, create:

```md
# MEMORY.md

## Durable Project Facts

## Architectural Decisions

## Security Constraints

## Coding Conventions

## Maintainer Preferences

## Known Constraints

## Update Policy

Update this file only when a durable project fact, architectural decision, security constraint, coding convention, maintainer preference, or known constraint is discovered or changed.

Do not copy chronological handoff entries into this file.
```

Use local `MEMORY.md` only for durable project facts, architectural decisions, security constraints, coding conventions, maintainer preferences, and known constraints.

---

## Local CHANGELOG_AI.md Starter

If `CHANGELOG_AI.md` does not exist in this project, create:

```md
# CHANGELOG_AI.md

This file is the chronological AI handoff ledger for this project.

## YYYY-MM-DD HH:MM TZ - Initialize AI handoff ledger

Task summary: Created the project-local AI handoff ledger.

Selected agent team: not applicable

Changes made:

- Created `CHANGELOG_AI.md`.

Files touched:

- `CHANGELOG_AI.md`

Commands/tests run:

- not applicable

Results: Project-local handoff ledger is ready.

Decisions made:

- Use this file for chronological AI handoffs in this repository.

Known issues:

- none

Next recommended steps:

- Continue with the requested task.

Notes for the next agent: Read the latest entry before making changes.

MEMORY.md update: not needed
```

Use local `CHANGELOG_AI.md` only for chronological task handoffs.

---

## Required Shutdown

Before completing work, stopping, switching tools, or reaching a context limit:

1. Update this project's `CHANGELOG_AI.md`.
2. Add a new handoff entry with task summary, selected agent team, changes made, files touched, commands/tests run, results, decisions made, known issues, next recommended steps, and notes for the next agent.
3. Review whether this project's durable memory changed.
4. If yes, update this project's `MEMORY.md`.
5. If no, state `MEMORY.md update: not needed` in the handoff entry.

A task is not complete until the local handoff entry is written.

---

## Project Overrides

If this repository needs instructions that differ from the global source, add them to this file under a clear `Project Overrides` section.

Keep overrides narrow. Universal instructions belong in the user-level global AI source, not in individual projects.
