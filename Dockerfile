ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}-alpine

WORKDIR /wg_be_exam

RUN apk add --no-cache bash curl vim build-base postgresql-dev

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /wg_be_exam/

# Project initialization:
RUN bash -c "poetry shell && poetry install --no-root"

# Creating folders, and files for a project:
COPY . /wg_be_exam

EXPOSE 5000
