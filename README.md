# API Technical Assessment

## Languages and Libraries

1. Python
2. Fast API

## Installation

```bash
    git clone https://gitlab.com/dodzireynard/api-technical-assessment.git
    cd api-technical-assessment/solution
    pip install -r requirements.txt
```

## Run Tests

Run the command below while in the `api-technical-assessment/solution` directory

```bash
python -m unittest discover -s tests
```

## Run without Docker

Run the command below while in the `api-technical-assessment/solution` directory

```bash
    alembic upgrade head # Run DB migrations.
    uvicorn app.main:app --reload # Run local dev  server.
```

Visit http://127:0.0.1:8000/docs

## Run using Docker

Run the command below while in the `api-technical-assessment` directory

```
docker compose -f docker-compose.yml up --build
```

Visit http://localhost:8000/docs
