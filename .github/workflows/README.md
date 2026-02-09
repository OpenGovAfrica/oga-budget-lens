# GitHub Actions Workflows

This directory contains the automated workflows for the OGA Budget Lens project.

## CI Pipeline (`ci.yml`)

The primary CI pipeline is designed to ensure code quality and data integrity. It triggers on pull requests to the `main` and `develop` branches.

### Jobs

1.  **Run Tests**
    - **Environment**: Ubuntu Latest, Python 3.11.
    - **Action**: Installs project dependencies and executes the test suite using `pytest`.
    - **Coverage**: Generates a coverage report using `pytest-cov` and uploads the results for analysis.

2.  **Validate JSON Schemas**
    - **Environment**: Ubuntu Latest, Python 3.11.
    - **Schema Validation**: Scans the `schemas/` directory and validates each file against JSON Schema standards.
    - **Data Validation**: Verifies that JSON files are syntactically correct and properly formatted.
    - **Tools**: Utilizes `jsonschema` and `check-jsonschema` for rigorous validation.

### Local Testing

To mirror these checks locally, you can run:

- **Tests**: `pytest --cov=app`
- **Schema Check**: `check-jsonschema --schemafile schemas/your_schema.json data/your_data.json`
