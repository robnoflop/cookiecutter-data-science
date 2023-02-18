FROM python:3.10-slim as base
RUN mkdir -p /app/data
RUN mkdir /app/code
RUN mkdir /app/model
COPY poetry.lock pyproject.toml README.md /app/code
RUN pip install poetry
WORKDIR /app/code
RUN poetry config virtualenvs.create false
RUN poetry install --only main

FROM base as root
COPY src/mylibcc /app/code/mylibcc

FROM root as test
RUN poetry install --only test
RUN mypy --strict .
RUN flake8 .
COPY src/tests tests
RUN pytest tests

# FROM root as build


# FROM root as build_docs