# API Technical Assessment

## Languages and Libraries

1. Python
2. Fast API

## Installation

```bash
    git clone ...
    cd 4thirapi/solution
```

## Running Tests

Run the command below while in the `4thirapi/solution` directory

```bash
python -m unittest discover -s tests
```

## Running without Docker

Run the command below while in the `4thirapi/solution` directory

```bash
    alembic upgrade head # Run DB migrations.
    uvicorn app.main:app --reload # Run local dev  server.
```

Visit http://127:0.0.1:8000/docs

## Running using Docker

Run the command below while in the `4thirapi` directory

```
docker compose -f docker-compose.yml up --build
```

Visit http://localhost:8000/docs
