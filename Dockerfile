# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app

# Install dependencies
RUN pip install flask

# Expose the application's port
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]