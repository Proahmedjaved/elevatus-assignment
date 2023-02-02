# FastAPI Dockerfile
FROM python:3.9.16

WORKDIR /app

COPY . .

RUN pip3 install pipenv

RUN pipenv install --system --deploy

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
