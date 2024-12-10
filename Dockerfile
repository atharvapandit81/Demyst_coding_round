# Use Python as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all the files from the host to the container
COPY . /app

# Define the default command to run the script
CMD ["python", "fixed_width_file.py"]
