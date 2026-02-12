# Contributing to OGA Budget Lens

Welcome to **OGA Budget Lens**! We are excited to have you contribute to this mission-critical tool for fiscal transparency in Africa.

### 📖 Read This First

Before you start setting up your environment, please ensure you have read the following documents to understand the project's vision, architecture, and standards:

1.  **[README.md](README.md)**: Overview of the project, core principles, and contributor roles.
2.  **[TECHNICAL_OVERVIEW.md](TECHNICAL_OVERVIEW.md)**: Deep dive into the problem statement and target architecture.
3.  **[PROJECT-STANDARD.md](PROJECT-STANDARD.md)**: Mandatory code quality, documentation, and communication standards.
4.  **[ROADMAP.md](ROADMAP.md)**: Current status and upcoming milestones.

Understanding these foundations is critical for ensuring your contributions align with the project's long-term goals.

---

## 🛠 Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## 🚀 Getting Started

### 1. Build the Environment

To build the Docker images for the first time or after updating `requirements.txt` or the `Dockerfile`, run:

```bash
docker compose build
```

### 2. Run the API Service

The API is built using FastAPI and serves as the main entry point for the application.

- **Start the API:**
  ```bash
  docker compose up -d api
  ```
- **Access the API:**
  The API will be available at `http://localhost:8000`.
- **API Documentation:**
  FastAPI automatically generates documentation at:
  - Swagger UI: `http://localhost:8000/docs`
  - ReDoc: `http://localhost:8000/redoc`

### 3. Run the Batch Pipeline

The batch pipeline processes all PDF documents in the `data/samples` directory.

- **Run the pipeline once:**
  ```bash
  docker compose run --rm pipeline
  ```
  _The `--rm` flag ensures the container is removed after it finishes execution._

---

## 📁 Data Management

The project uses a host-mounted volume for data. The local `./data` directory is mapped to `/data` inside the containers.

- Place your PDF files in `./data/samples/`.
- The pipeline will automatically detect and process them when run.

---

## 💻 Development Workflow

### Running Tests

To run the project's test suite inside the Docker environment:

```bash
docker compose run --rm api pytest
```

### Executing Commands in a Running Container

If the API service is running, you can execute commands inside it:

```bash
# Open a shell inside the api container
docker compose exec api bash

# Run the pipeline script manually
docker compose exec api python app/pipelines/batch.py /data/samples
```

### Viewing Logs

To see the logs from the running API service:

```bash
docker compose logs -f api
```

---

## 🛑 Stopping and Cleaning Up

It is important to properly shut down your Docker environment when finished.

### 1. Stop and Remove Containers

To stop the running services and remove the containers and networks created by `up`:

```bash
docker compose down
```

### 2. Stop Containers (without removing)

If you want to stop the containers but keep them (e.g., to restart later):

```bash
docker compose stop
```

### 3. Deep Clean

To remove images and orphaned containers as well:

```bash
docker compose down --rmi all --remove-orphans
```

---

## 📄 Project Structure

- `app/main.py`: The FastAPI application entry point.
- `app/pipelines/batch.py`: The batch processing logic.
- `src/oga_budget_lens/`: Core library code for PDF processing.
- `data/`: Local data storage (mounted into containers).
- `tests/`: Unit and integration tests.

---

## 📝 Coding Standards

- Follow PEP 8 for Python code.
- Ensure all new features are covered by tests.
- Update documentation in the `docs/` directory or READMEs if you change functionality.

Thank you for contributing!
