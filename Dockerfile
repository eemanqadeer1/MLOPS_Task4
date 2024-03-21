# Use Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy necessary files to the container
COPY app.py client.py Cereals.py Cereals.joblib requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
