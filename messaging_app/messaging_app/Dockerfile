# Use official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Default command
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "-p", "8000:8000"]
