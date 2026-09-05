---
name: docs-expert
description: >
  Expert in agile, precise, and strategic software project documentation. Covers READMEs,
  architecture docs, API/data-model docs, code conventions, Architecture Decision Records (ADRs),
  functional specifications, business rules, and stakeholder-facing decision documents. Keeps
  documentation lightweight and living (updated alongside the code, never a stale one-off), and
  enforces a strict separation between TECHNICAL documentation and BUSINESS/FUNCTIONAL documentation
  so each audience gets exactly what it needs without duplication.
  Trigger: When the user says "documenta", "documentación", "escribe un ADR", "documento de decisión",
  "readme", "especificación funcional", "reglas de negocio", "documento técnico", "documenta la
  arquitectura", "documenta la api", "actualiza la documentación", "document this", "write a README",
  "write an ADR", "architecture decision record", "functional spec", "business rules doc",
  "decision document", "document the architecture", "document the API", "update the docs", or any
  variant expressing intent to create or maintain documentation for a software project.
license: Apache-2.0
metadata:
  author: brioslabs
  version: "1.0.0"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

## When to Use

- User asks to document a project, feature, architecture, API, or data model.
- User asks to write or update a README, onboarding doc, or code-convention guide.
- User asks to record a technical decision (ADR) or a business/product decision.
- User asks to write a functional specification or business-rules document for stakeholders.
- Documentation exists but is stale, duplicated, or mixes technical and business content.

**Don't use this skill for**: writing the code itself (use the relevant `*-expert` skill), or
one-off inline code comments — those aren't project documentation.

## Critical Patterns

### 1. Documentation is agile, not waterfall

- Docs are **living artifacts**: update them in the same PR/commit as the change they describe,
  never as a separate "documentation sprint".
- Prefer short, focused files over one giant manual — smaller files have lower update friction
  and lower merge-conflict risk.
- No filler: every sentence must inform a decision or an understanding. If a reader wouldn't
  miss a sentence, cut it.
- Write for two readers at once: a skim (headings, tables, bullets) and a deep read (the "why").

### 2. Strict independence: TECHNICAL vs BUSINESS documentation

This is the core rule of this skill. Two documentation lines, never mixed in the same file:

| | **Technical** (`docs/technical/`) | **Business** (`docs/business/`) |
|---|---|---|
| Answers | "How does it work?" | "Why does it exist / why this choice?" |
| Audience | Engineers, new devs, ops | Stakeholders, PM, non-technical readers |
| Content | Architecture, APIs, data models, code conventions, infra, ADRs | Objectives, stakeholders, requirements, business rules, decision rationale in plain language |
| Updates when | Code/architecture/API/schema changes | Scope, requirement, or business rule changes |
| Owner | Whoever makes the technical change | Whoever makes the product/business call |

Concrete folder convention (create under the project root, not under this skill):

```text
docs/
├── technical/
│   ├── architecture.md          # system overview, components, data flow
│   ├── api/                     # per-service or per-domain API reference
│   ├── data-model.md            # entities, relationships
│   ├── conventions.md           # code style, naming, folder layout
│   └── decisions/
│       └── ADR-0001-title.md    # see assets/adr-template.md
└── business/
    ├── overview.md               # product objective, target users, scope
    ├── requirements/              # functional specs, one file per feature area
    ├── glossary.md                # domain terms in plain language
    └── decisions/
        └── DEC-0001-title.md     # see assets/decision-template.md
```

Rationale: separate top-level folders (not just separate sections in one file) give each line
its own update cadence, its own reviewers, and prevent a technical PR from silently drifting
business content (or vice versa).

### 3. Cross-reference, never duplicate

- An ADR that exists because of a business need adds one line: `Business context: see
  ../../business/decisions/DEC-0003-title.md`.
- A business decision doc that has a technical implementation adds one line: `Technical
  implementation: see ../../technical/decisions/ADR-0004-title.md`.
- Never restate the other line's content — link to it. If you catch yourself copying a
  paragraph across the two trees, that content belongs in exactly one of them; link from the other.

## Code Examples

Cross-reference line to put at the bottom of an ADR:

```markdown
Business context: see [../../business/decisions/DEC-0003-self-checkout.md](../../business/decisions/DEC-0003-self-checkout.md)
```

Cross-reference line to put at the bottom of a business decision doc:

```markdown
Technical implementation: see [../../technical/decisions/ADR-0004-async-checkout-queue.md](../../technical/decisions/ADR-0004-async-checkout-queue.md)
```

## Useful Commands

```bash
# Scaffold the two documentation trees in a project that has none yet
mkdir -p docs/technical/api docs/technical/decisions docs/business/requirements docs/business/decisions

# Next ADR/decision number (zero-padded, sequential per folder)
ls docs/technical/decisions | grep -c ADR- # -> use next number for ADR-000N
ls docs/business/decisions | grep -c DEC-  # -> use next number for DEC-000N
```

## Resources

- **Templates**: See [assets/adr-template.md](assets/adr-template.md) for technical decision records.
- **Templates**: See [assets/decision-template.md](assets/decision-template.md) for business/functional decision documents.
