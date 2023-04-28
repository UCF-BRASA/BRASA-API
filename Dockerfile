# Base image
FROM python:3.11

# Set working directory
WORKDIR /src

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# COPY .env ./

# Install poetry
RUN pip install --upgrade pip \
 && pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --only main --no-root

# Copy source code
COPY ./src /src

# Expose port 8080
EXPOSE 8080

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]