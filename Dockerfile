# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency files into the container
# Use ADD if you have compressed files or need automatic extraction
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8000 available to the world outside this container
# Change this if your app runs on a different port (e.g., 5000 for Flask)
EXPOSE 8000

# Run the command when the container launches
# Replace 'app.py' and its arguments with the actual start command (e.g., gunicorn)
CMD ["python", "app.py"]