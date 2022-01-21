# API Technical Assessment

## Languages and Libraries

1. Python 3.9+
2. Fast API

## Installation

```bash
    git clone https://github.com/dodziraynard/api-technical-assessment.git
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

Visit [http://127:0.0.1:8000/docs](http://127:0.0.1:8000/docs)

## Run using Docker

Run the command below while in the `api-technical-assessment` directory.
Please make sure you have docker and docker compose setup and running.

```
docker compose -f ../docker-compose.yml up --build
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs)
