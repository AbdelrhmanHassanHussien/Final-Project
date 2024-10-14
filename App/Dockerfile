
# Build Stage
FROM python:3.11-alpine AS build

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

# Create and set working directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache build-base

# Copy requirements file and install dependencies
COPY requirements.txt . 

# Upgrade pip and setuptools to a secure version
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools==70.0.0 \
    && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Final Stage
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

# Create and set working directory
WORKDIR /app

# Install setuptools in the final image
RUN pip install --upgrade setuptools==70.0.0

# Copy installed dependencies from the build stage
COPY --from=build /usr/local /usr/local

# Copy application code from the build stage
COPY --from=build /app /app

# Expose the port the application runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]