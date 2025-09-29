# Use latest Python 3.12 slim image (or 3.11 if you prefer)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY scripts/ingest.py .
COPY requirements.txt .
COPY .env .

# Pre-create the data folder
RUN mkdir -p /app/data

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command
CMD ["python", "ingest.py"]
