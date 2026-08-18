---
name: skill-creator
description: >
  Creates new AI agent skills following the Agent Skills specification for brioslabs repositories.
  Trigger: When user asks to create a new skill, add agent instructions, or document patterns for AI.
license: Apache-2.0
metadata:
  author: brioslabs
  version: "1.0.0"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

## When to Create a Skill

Create a skill when:
- A pattern is used repeatedly and AI needs guidance.
- Project-specific conventions differ from generic best practices.
- Complex workflows need step-by-step instructions.
- Decision trees help AI choose the right approach.

**Don't create a skill when:**
- Documentation already exists (create a reference instead).
- Pattern is trivial or self-explanatory.
- It's a one-off task.

---

## Skill Structure

```text
skills/{skill-name}/
├── SKILL.md              # Required - main skill file
├── assets/               # Optional - templates, schemas, examples
│   ├── template.py
│   └── schema.json
└── references/           # Optional - links to local docs
    └── docs.md
```

---

## SKILL.md Template

```markdown
---
name: {skill-name}
description: >
  {One-line description of what this skill does}.
  Trigger: {When the AI should load this skill}.
license: Apache-2.0
metadata:
  author: brioslabs
  version: "1.0.0"
---

## When to Use

{Bullet points of when to use this skill}

## Critical Patterns

{The most important rules - what AI MUST know}

## Code Examples

{Minimal, focused examples}

## Commands

```bash
{Common commands}
```

## Resources

- **Templates**: See [assets/](assets/) for templates.
- **References**: See [references/](references/) for checklists.
```
