# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file (if you have one) or install Flask directly
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the app
CMD ["python", "app/main.py"]

