# Base image
FROM python:3.11

ARG PORT=8080

# Set working directory
WORKDIR /src

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN pip install --upgrade pip \
 && pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --only main --no-root

# Copy source code
COPY ./src /src

# Expose port 8080
EXPOSE ${PORT}

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", $PORT]