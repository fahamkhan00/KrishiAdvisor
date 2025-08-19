# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential cmake python3-dev wget && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install llama-cpp-python
RUN pip install llama-cpp-python

# Copy your project files into container
COPY . /app

# Download Mistral model into llama.cpp/models/ BEFORE installing requirements
WORKDIR /app/llama.cpp/models/
RUN wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf

# Back to app root
WORKDIR /app

# Install Python dependencies (after model is downloaded)
RUN pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run your Streamlit app (replace main.py if needed)
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
