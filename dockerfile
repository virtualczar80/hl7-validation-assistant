# Base Python image
FROM python:3.13-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first (better build caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]