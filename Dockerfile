# Use a Python base image as the project is Python-based.
FROM python:3.8-slim

# Install Git
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/ShubhangKhandelwal/LinkedIn-Analyzer.git /app

# Change the working directory to the cloned repository
WORKDIR /app

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
