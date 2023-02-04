<!-- Generate Readme for fastapi appication with mongo db using pipenv -->


[![testing](https://github.com/Proahmedjaved/elevatus-assignment/actions/workflows/testing.yml/badge.svg?branch=main)](https://github.com/Proahmedjaved/elevatus-assignment/actions/workflows/testing.yml) [![codecov](https://codecov.io/gh/Proahmedjaved/elevatus-assignment/branch/main/graph/badge.svg?token=99L5K24GKD)](https://codecov.io/gh/Proahmedjaved/elevatus-assignment)
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

# Test

<!-- test application -->

```bash
pytest
```
## Code Coverage

<!-- test application -->

```bash
coverage run -m pytest
```

<!-- generate report -->

```bash
coverage report
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
