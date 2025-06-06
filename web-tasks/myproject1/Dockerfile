# Use a multi-stage build to keep the final image small and secure
FROM python:3.13.3-slim-bookworm AS base
# Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# # Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set the working directory in the container
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .
# Install the dependencies in a separate stage to keep the final image clean
FROM base AS builder
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code from the base stage
FROM builder AS final
COPY . .

# # Change ownership of the application files to the non-root user
RUN chown -R appuser:appgroup /app
# # Switch to the non-root user
USER appuser

# Expose the port the application will run on
EXPOSE 8000
# Set the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]        
# Note: The CMD command assumes you have a Django application with a manage.py file.
# If you want to use a production-ready server like Gunicorn, you can replace the CMD line with:
# CMD ["gunicorn", "--bind", "0.0.0:8000", "myproject1.wsgi:application"]
# Example of a Dockerfile for a Django application with best practices and security














