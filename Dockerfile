# Start with a Python base image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy the local content into the container
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
