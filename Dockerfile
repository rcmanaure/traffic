FROM python:3.11-slim-bullseye

WORKDIR /app/

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    # python3-dev \
    # gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
# Create and activate virtual environment
COPY requirements.txt /app/requirements.txt
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN /venv/bin/pip install --upgrade pip wheel setuptools
RUN /venv/bin/pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy project
COPY . .
RUN mkdir -p /tmp/shm && mkdir /.local && chmod 777 /tmp/shm /.local
EXPOSE 8000
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
