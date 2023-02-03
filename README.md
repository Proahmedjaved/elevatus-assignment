<!-- Generate Readme for fastapi appication with mongo db using pipenv -->

# FastAPI with MongoDB

This is a simple example of how to use FastAPI with MongoDB.

## Installation

<!-- copy example env file -->

```bash
cp example.env .env
```

<!-- install pipenv -->

```bash
pip install pipenv
```

<!-- install dependencies -->

```bash
pipenv install
```

<!-- activate virtual environment -->

```bash
pipenv shell
```

<!-- run application -->

```bash
uvicorn main:app --reload
```

## Docker Compose

<!-- build docker image -->

```bash
docker-compose build
```

<!-- run docker container -->

```bash
docker-compose up
```

## Docker

<!-- build docker image -->

```bash
docker build -t fastapi-mongodb .
```
