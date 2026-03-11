## Project 2: AI-Assisted Budget Document Parsing

**Goal:**
Create an auditable, human-verifiable pipeline to extract structured, standardized budget data from unstructured government budget documents (PDFs), optimized for African contexts.

**Before you start, please ensure you have checked the project standard for all 3 projects [here](https://github.com/OpenGovAfrica/gsoc/blob/main/docs/project-standard.md)**

This project must support:

* Scanned and digital PDFs
* Multiple languages (English, French, Portuguese minimum)
* Weak formatting and inconsistent layouts
* Cross-country comparison
* Strong provenance and human verification

---

## Phase 1: Infrastructure & Core Data Modeling

### 1.1 Parsing Pipeline Setup

* [ ] Containerize a Python-based parsing environment
* [ ] Define a **canonical Budget Line Item schema**, including:

  * fiscal_year
  * country_code (ISO-3166)
  * currency_code (ISO-4217)
  * budget_level (vote / ministry / program / subprogram / line_item)
  * description (raw + cleaned)
  * amount_nominal
  * amount_normalized (optional)
  * parent_line_item_id (for hierarchy)
  * page_number
  * confidence_score

📌 **Design Note (Non-Blocking):**
Hierarchical budgets should be represented using explicit parent–child relationships, not inferred from indentation alone. All design trade-offs must be documented in `DATA_MODEL_DECISIONS.md`.

- budget_version:
  - original
  - supplementary
  - revised
- revision_sequence (nullable integer)

📌 Design Note:
This does not require full support for revisions, but schemas must not prevent it.

---

### 1.2 Document Ingestion & OCR

* [ ] Detect PDF type:

  * digital text-based
  * scanned / image-based
* [ ] Integrate OCR (e.g. Tesseract, PaddleOCR)
* [ ] Preserve:

  * page numbers
  * bounding boxes
  * original text fragments

- Detect and store document language(s)
- Allow multiple languages per document

📌 **Africa Context Note:**
OCR accuracy varies widely across languages and print quality. The system must retain raw OCR output for traceability and human correction.

---

### 1.3 Layout Analysis

* [ ] Use LayoutParser or Unstructured to detect:

  * headers
  * footers
  * tables
  * narrative sections
* [ ] Classify detected regions with confidence scores
* [ ] Store layout metadata for debugging and review

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 2: Table & Structure Extraction

### 2.1 Table Extraction Engine

* [ ] Extract tables using Camelot or Tabula
* [ ] Handle:

  * multi-page tables
  * split headers
  * merged cells
* [ ] Normalize extracted tables into intermediate data frames

📌 **Validation Rule:**
All extracted tables must retain a reference to their source page(s) and bounding box.

---

### 2.2 Hierarchy Reconstruction

* [ ] Detect budget hierarchies using:

  * indentation
  * numbering patterns
  * repeated headers
* [ ] Link child rows to parent budget items
* [ ] Flag ambiguous hierarchies for human review

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 3: LLM-Assisted Cleaning & Classification

**📌 AI Safety Rule:**
LLMs **must not** infer, invent, or interpolate financial amounts or fiscal metadata.
They may **only** clean, normalize, or classify existing extracted text.

### 3.1 Text Normalization Layer

* [ ] Use an LLM to:

  * clean OCR artifacts
  * normalize inconsistent descriptions
* [ ] Preserve original text alongside cleaned text

- Store (This can be metadata only; no infra explosion):
  - model name/version
  - prompt version identifier
  - timestamp of inference

📌 **Safety Rule:**
LLMs must never invent amounts or fiscal metadata.

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

### 3.2 Functional Classification (COFOG)

* [ ] Map budget line items to:

  * COFOG categories (where applicable)
* [ ] Store:

  * predicted category
  * confidence score
  * explanation / rationale (if available)

📌 **Design Note:**
Manual override must always be possible. 

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.


---

## Phase 4: Provenance, Audit & Trust

### 4.1 Source & Evidence Model

* [ ] Implement `Source` model:

  * source_file
  * source_url (if published online)
  * page_number
  * extraction_method (OCR / digital)
* [ ] Link every budget line item to at least one source

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

### 4.2 Human-in-the-Loop Workflow

* [ ] Build a review UI showing:

  * original PDF page
  * extracted table
  * editable structured fields
* [ ] Track:

  * AI-generated values
  * human edits
  * editor identity
  * timestamps

📌 **Trust Rule:**
Published datasets must distinguish between AI-extracted and human-verified entries.

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 5: Validation & Quality Assurance

### 5.1 Arithmetic & Structural Validation

* [ ] Balance Checker:

  * child rows must sum to parents
* [ ] Detect:

  * negative or zero anomalies
  * missing totals
  * duplicate line items

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

### 5.2 Semantic Validation

* [ ] Detect suspicious patterns:

  * sudden spikes year-over-year
  * mismatched currency symbols
* [ ] Flag inconsistencies for review

---

### 5.3 Automated Test Suite

* [ ] Unit tests for:

  * schema validation
  * hierarchy logic
* [ ] Integration tests with sample PDFs
* [ ] CI enforcement

#### 5.4 Currency & Normalization Metadata 

- [ ] Store exchange_rate_source (e.g. IMF, World Bank)
- [ ] Store conversion_date
- [ ] Clearly distinguish nominal vs normalized values

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 6: Export, CLI & Interoperability

### 6.1 Batch CLI Tool

* [ ] Process directories of PDFs
* [ ] Export to:

  * validated JSON
  * UTF-8 CSV
  * Excel
* [ ] Support flags for:

  * country
  * fiscal year
  * language

---

### 6.2 Interoperability

* [ ] Ensure outputs are compatible with:

  * OpenSpending-style datasets
* [ ] Document schema clearly

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 7: Evaluation & Metrics

* [ ] Define evaluation metrics:

  * extraction accuracy (sampled)
  * human correction rate
  * balance pass rate
* [ ] Provide a report on:

  * model strengths
  * common failure modes

- Document common failure modes
- Ensure pipeline fails loudly and flags unprocessable documents
- No silent partial exports

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Phase 8: Finalization & Handover

* [ ] Provide demo datasets from at least:

  * one Anglophone country
  * one Francophone or Lusophone country

* [ ] Produce:

  * `ARCHITECTURE.md`
  * `DATA_MODEL_DECISIONS.md`
  * `CONTRIBUTING.md`
 
* [ ] Identify 5+ “Good First Issues”

- Define default open data license for extracted outputs
- Document any country-specific reuse constraints

**Phase Complete When:**
- Pipeline successfully processes at least one real-world PDF end-to-end with provenance.

---

## Definition of Done (Project 2)

* [ ] Works on scanned and digital PDFs
* [ ] Supports multiple languages
* [ ] Every number has provenance
* [ ] Human verification is first-class
* [ ] Exports are standardized and validated
* [ ] Pipeline is test-covered and documented
