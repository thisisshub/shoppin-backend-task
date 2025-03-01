FROM python:3.13-alpine

WORKDIR /backend

# INSTALL POETRY
RUN pip install poetry

# COPY POETRY.LOCK AND POETRY.TOML
COPY pyproject.toml poetry.lock ./

# INSTALL DEPENDENCIES
RUN poetry install --no-root

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]