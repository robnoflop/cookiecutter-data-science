FROM python:3.10-slim as base
    RUN mkdir /ml/code
    RUN pip install poetry
    RUN poetry config virtualenvs.create false
    WORKDIR /ml/code

    COPY poetry.lock pyproject.toml README.md ./
    RUN poetry install --only main

FROM base as testbase
    RUN poetry install --only test

