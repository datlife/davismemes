FROM python:3.7-alpine
LABEL maintainer="Dat Nguyen" \
      email="hi@dat.works"

# Install pipenv
RUN pip3 install pipenv

# -- Install Application into container:
RUN set -ex && mkdir /app
WORKDIR /app

# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system