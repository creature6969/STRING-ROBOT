FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Expose the port the app will run on
EXPOSE 8000

# Define the command to run the app
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000"]
