### OpenGov Africa Project Standards and Contributor Requirements

All OpenGov Africa (OGA) projects must adhere to the following standards to ensure long-term maintainability, transparency, and ecosystem reuse. These standards apply to all contributors, regardless of entry point or experience level.

---

### Individual Ownership and Collaborative Development

OpenGov Africa strongly encourages open collaboration, peer learning, and knowledge sharing across the community. Contributors are expected to discuss ideas publicly, help others troubleshoot, and review one another’s work.

At the same time, **each contributor is accountable for the work they submit under their name**. Code contributions, technical decisions, and deliverables must reflect the contributor’s own understanding and execution, even when informed by discussion or feedback from others.

Early foundational work (such as initial scaffolding, tooling, and setup tasks) is intentionally collaborative and should be treated as a learning and coordination phase. Contributors are encouraged to work together at this stage to accelerate learning and align on best practices. However, each contributor should still demonstrate the ability to independently design, implement, and document solutions.

This balance ensures:

* Knowledge is shared openly
* Code quality remains attributable and reviewable
* Contributors demonstrate real technical ownership

---

### 1. Technical Documentation

Every OGA project repository must maintain the following core files at the repository root:

* **README.md**
  Must clearly explain the project vision, scope, and intended users.
  Should include visual UI mockups where applicable and a “Quick Start” section that allows a new contributor to run the project locally in under 5 minutes.

* **ARCHITECTURE.md**
  Describes system design and technical decisions, including:

  * Technology stack choices
  * Data flow and component interactions
  * Relationships between services (e.g. frontend, backend, database, workers)

* **CONTRIBUTING.md**
  Defines how to contribute to the project, including:

  * Local development setup
  * Branching and commit strategy
  * Pull request and review requirements

Documentation is not optional and must evolve alongside the codebase.

---

### 2. Code Quality and Automation

All projects must enforce automated quality checks from the first commit.

| Category        | Tooling                        | Requirement                                         |
| --------------- | ------------------------------ | --------------------------------------------------- |
| Linting         | Ruff (Python) / ESLint (JS)    | Zero linting errors allowed on the main branch      |
| Formatting      | Black (Python) / Prettier (JS) | Enforced via pre-commit hooks or CI                 |
| Testing         | PyTest / Jest                  | Minimum 70% coverage for business-critical logic    |
| Version Control | Git                            | Use Conventional Commits (`feat:`, `fix:`, `docs:`) |

Automation should be treated as foundational infrastructure, not an afterthought.

---

### 3. API and Data Standards

To ensure interoperability and reuse across the civic tech ecosystem:

* **Self-Documenting APIs**
  All backend services must expose OpenAPI/Swagger documentation, ideally accessible via `/docs`.

* **Standardized Schemas**

  * **Public Office / People Data**: Follow the Popolo Specification
  * **Budget & Financial Data**: Output validated JSON or UTF-8 CSV
  * **Geospatial / Service Delivery Data**: Use GeoJSON for all spatial objects

* **Provenance and Auditability**
  Every data record must include a `source_url`, `evidence_ref`, or equivalent field that clearly identifies the origin of the data.

Data without provenance is considered incomplete.

---

### 4. Communication and Workflow

* **Public-First Development**
  All work should happen in public branches and repositories. Open draft pull requests early to receive feedback on design and architecture, not just final code.

* **Issue-Driven Development**
  Every pull request must be linked to a GitHub Issue (e.g. `Closes #12`) describing the problem being solved.

* **Regular Status Updates**
  Contributors working on active projects are expected to provide periodic written updates (weekly where applicable) covering:

  * Progress made
  * Current blockers or risks
  * Planned next steps

Clear communication is a core contributor responsibility.

---

### 5. Project Completion and Handover

A project or major milestone is considered complete only when it includes:

* **Functional Demo**
  A working deployment or staging environment demonstrating core functionality.

* **Recorded Walkthrough**
  A short video (≈5 minutes) showing:

  * Key features
  * System flow
  * High-level code structure

* **Sustainability Roadmap**
  A forward-looking list of at least five well-scoped “Good First Issues” to enable future contributors to onboard quickly.

Completion is defined by usability and clarity, not just merged code.

---

### Phase 0: Foundational Project Scaffold

Before implementing project-specific features, all projects must complete the following baseline setup to ensure scalability and contributor friendliness.

| Task Item           | Technical Goal / Deliverable                                                  |
| ------------------- | ----------------------------------------------------------------------------- |
| Dockerization       | A docker-compose setup that runs the app and dependencies with one command    |
| CI Pipeline         | GitHub Actions running linting and tests on every push and pull request       |
| Environment Config  | A `.env.example` file documenting required environment variables              |
| Base Authentication | Basic auth (JWT or session-based) for protected or admin routes               |
| UI Foundation       | A shared design system (e.g. Tailwind or Material UI) where a frontend exists |

This phase establishes a stable foundation for all future work.

---

### Definition of Done

A task or feature is considered complete only when all of the following are satisfied:

1. **Code**
   Clean, readable, and compliant with project linting and formatting rules.

2. **Tests**
   Appropriate unit and/or integration tests with passing CI checks.

3. **Documentation**
   Relevant updates to README.md, ARCHITECTURE.md, and API docs.

4. **Migrations**
   Valid and reviewed database migration files for any schema changes.

5. **Review**
   At least one approved code review.
   Peer reviews, collaborative feedback, and assisting other contributors are strongly encouraged.
