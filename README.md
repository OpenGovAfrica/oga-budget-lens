### OGA-budget-lens

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

---

### Contributors & Roles

This project follows an individual-ownership, collaborative-development model across all phases of work and maintains explicit attribution for all contributors. Contributors are encouraged to collaborate through discussion, reviews, and coordination at every stage of the project. However, all implemented work must have clearly attributable ownership.

Each contributor is credited with the specific components, tasks, or deliverables they owned or led. Participation, discussion, or review alone does not imply ownership.

| Contributor | Role / Focus Area | Owned Deliverables |
|------------|------------------|--------------------|
| Name / GitHub | Backend, Frontend, Data, Infra, Research | Clearly scoped features, services, or setup tasks |
| Divyanshu-Off | Infra | CI/CD pipeline for the project |
| Divyanshu-Off | Backend, Infra | Containerization of parsing environment (Docker & Compose), FastAPI scaffolding, and contributor documentation |

This table must be kept up to date as the project evolves, from Phase 0 through final delivery. Phase-level credit is insufficient on its own; ownership must always be traceable to concrete deliverables, from initial scaffolding (Phase 0) through final handover.

**Clarification on Collaboration and Ownership (All Phases)**

From Phase 0 through the final phase, contributors may not jointly claim the same implementation output unless responsibilities are explicitly separated and documented. Collaboration should strengthen implementation quality, not dilute accountability.

---

### Definition of Done

A task or feature is considered complete only when all of the following are satisfied:

1. Code is clean, readable, and compliant with project linting and formatting rules.
2. Appropriate unit and/or integration tests are included and CI passes.
3. Relevant documentation is updated (README, ARCHITECTURE, API docs where applicable).
4. Database migrations are provided and reviewed if schema changes are involved.
5. The Pull Request has received at least one peer review and maintainer approval.

---

### Relationship to Tech Programs, Hackathons & Internships

This project may be developed in part through tech programs. If you are contributing through GSoC, MLH, Outreachy etc, please find your [project standard here](https://github.com/OpenGovAfrica/gsoc/blob/main/docs/project-standard.md) & roadmap [here](https://github.com/OpenGovAfrica/gsoc/issues/20).
_If this becomes obselete please raise an issue for_

Contributors are expected to:

- Build reusable, well-documented components
- Respect long-term maintenance needs
- Treat programs as an entry point, not a finish line

The roadmap and contribution guidelines are designed for continuity beyond any single program.

### GSoC Compatibility Note

GSoC compatibility: Contributors may collaborate through discussion and peer review, but all submitted work must have clear individual ownership and be attributable to a single contributor for evaluation.

---

### Maintainer Enforcement Guidelines

These guidelines apply from Phase 0 through final project delivery.

Maintainers are responsible for ensuring clear ownership and accountability throughout the project lifecycle. When reviewing work, maintainers should verify that:

1. Every pull request has a clearly identifiable primary owner.
2. Each deliverable, regardless of phase, is attributable to a specific contributor.
3. The README “Contributors & Roles” section reflects actual implementation ownership, not participation alone.
4. Multiple contributors are not credited for the same deliverable unless roles and responsibilities are explicitly differentiated.
5. Collaboration is demonstrated through reviews, discussions, and coordination — not shared ownership of identical outputs.

If ownership is unclear at any stage, maintainers should request clarification or restructuring before merging.
Clear ownership is required for all phases to ensure sustainability, accountability, and long-term project health.

---

### Repository Structure (Evolving)

Expected top-level documents include:

- `TECHNICAL_OVERVIEW.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `DATA_MODEL_DECISIONS.md`
- `ARCHITECTURE.md`

Structure will stabilize as implementation progresses.

## Getting Started

### Prerequisites

- **Python 3.10 or higher**
- **System dependencies** (for PDF processing):
  - Tesseract OCR: [Installation guide](https://github.com/tesseract-ocr/tesseract)
  - Ghostscript: [Installation guide](https://www.ghostscript.com/download/gsdnld.html)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/OpenGovAfrica/oga-budget-lens.git
   cd oga-budget-lens
```

2. **Create a virtual environment** (recommended)
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Verify your setup**
```bash
   python setup_check.py
```

   You should see: `✓ All checks passed! Environment ready.`

### Quick Start

Once your environment is set up, you can explore the project structure and review open issues to start contributing.

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
