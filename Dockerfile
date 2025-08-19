FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Cloud Run expects the service to listen on $PORT (default 8080)
EXPOSE 8080

# Run Gunicorn and point it to "app" inside wsgi.py
CMD exec gunicorn --bind :$PORT --workers 2 wsgi:app
