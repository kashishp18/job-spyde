# Use /app (singular) as is standard
WORKDIR /app

# Copy everything from apps/agent into /app
COPY . .

# Set PYTHONPATH to the current workdir
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]