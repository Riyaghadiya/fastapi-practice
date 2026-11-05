# Use an official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Set default environment
ENV PYTHONUNBUFFERED=1

# Expose API port
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]