FROM python:3.11-slim


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# change <botify> to your project name
RUN mkdir /usr/src/portfolio
WORKDIR /usr/src/portfolio




COPY pyproject.toml  ./

RUN pip install poetry \
    && pip --version


RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /usr/src/portfolio/portfolio

