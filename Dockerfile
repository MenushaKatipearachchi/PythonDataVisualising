# Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY . /code/

# This command runs the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
