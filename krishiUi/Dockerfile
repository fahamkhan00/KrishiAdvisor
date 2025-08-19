# Use Python 3.9 (as per runtime.txt)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirement files
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the whole project
COPY . /app

# Expose FastAPI port
EXPOSE 5000

# Run app with Uvicorn (from Procfile)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000"]
