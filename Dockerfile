# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the app runs
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
