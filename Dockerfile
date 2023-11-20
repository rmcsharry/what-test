FROM python:3.12

ARG WORKDIR="/app"

# Configure Python to not buffer "stdout" or create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ${WORKDIR}
# Copy app files into container
COPY . ${WORKDIR}

# Install dependencies
# install poetry
RUN pip install poetry
# disable virtualenv for peotry
RUN poetry config virtualenvs.create false
# install dependencies
RUN poetry install

CMD uwsgi --module=whattest.wsgi --http=0.0.0.0:80