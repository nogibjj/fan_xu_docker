# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app

# Install dependencies
RUN pip install flask
RUN pip install requests

# Expose the application's port
EXPOSE 5000

ENV FLASK_APP=app.py

# Define the command to run the application
CMD ["python", "app.py"]