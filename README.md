### oga-budget-lens

[![CI Tests](https://github.com/OpenGovAfrica/oga-budget-lens/actions/workflows/test.yml/badge.svg)](https://github.com/OpenGovAfrica/oga-budget-lens/actions/workflows/test.yml)

**OGA-budget-lens** OGA-budget-lens is an AI-assisted tool for turning complex & unstructured government budget documents (PDFs) into structured, auditable, and human-verifiable data, with a focus on African public finance and accountability.

The project prioritizes **trust, provenance, and reviewability** over opaque automation.

This repository is at an early stage and focuses on laying strong technical and governance foundations.

### Why This Project Exists

Across many African countries, government budgets are published as:

- Scanned or poorly formatted PDFs
- Documents with weak or inconsistent structure
- Multi-language texts (English, French, Portuguese, and others)
- Files that are difficult to compare across years or countries

Most existing extraction approaches:

- Lose links to original sources
- Hide uncertainty or errors
- Or rely on AI systems that infer missing fiscal data

Budget Lens takes a different approach:  
**every extracted number must be traceable, reviewable, and correctable by a human.**

### Core Principles

- Provenance is non-negotiable
- Human verification is first-class
- AI assistance is constrained and auditable
- Ambiguity must be surfaced, not hidden
- Cross-country comparison is a design requirement

### What This Repository Contains

This repository will evolve to include:

- A provenance-aware parsing pipeline for budget PDFs
- A canonical budget line item data model
- Validation and quality assurance tooling
- Human-in-the-loop review workflows
- Standardized export formats for reuse

At present, the repository focuses on:

- Architecture and data model design
- Defining safety and trust constraints
- Preparing for initial implementation work

### Project Status

- No production pipeline yet
- No fixed development environment
- Active design and early implementation phase

Early contributors will help define:

- Core schemas
- Tooling choices
- Validation rules
- Repository structure

### Relationship to Tech Programs, Hackathons & Internships

This project may be developed in part through tech programs. If you are contributing through GSoC, please find your [project standard here](https://github.com/OpenGovAfrica/gsoc/blob/main/docs/project-standard.md) & roadmap [here](https://github.com/OpenGovAfrica/gsoc/issues/20)

Contributors are expected to:

- Build reusable, well-documented components
- Respect long-term maintenance needs
- Treat programs as an entry point, not a finish line

The roadmap and contribution guidelines are designed for continuity beyond any single program.

### Repository Structure (Evolving)

Expected top-level documents include:

- `TECHNICAL_OVERVIEW.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `DATA_MODEL_DECISIONS.md`
- `ARCHITECTURE.md`

Structure will stabilize as implementation progresses.

### How to Get Involved

- Read the roadmap to understand project direction
- Check issues labeled `good first issue` or `design`
- Join discussions around data models and validation
- Propose improvements via issues or pull requests

See `CONTRIBUTING.md` for details.

### Governance and Sustainability

This project is maintained under the OpenGovAfrica ecosystem.

Design decisions are expected to:

- Be documented
- Favor clarity over cleverness
- Support reuse by journalists, researchers, and civic technologists
