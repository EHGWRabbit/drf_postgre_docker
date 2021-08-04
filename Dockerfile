
FROM python:3.8

WORKDIR /blog

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY Pipfile Pipfile.lock /blog/
RUN pip install pipenv && pipenv install --system


COPY . /blog/