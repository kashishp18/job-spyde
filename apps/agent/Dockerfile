FROM mcr.microsoft.com/playwright/python:v1.46.0-jammy

WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers for scraping
RUN playwright install chromium --with-deps

# Copy everything
COPY . .

# Render uses the PORT environment variable
ENV PORT=10000
EXPOSE 10000

# Use shell form to allow environment variable expansion
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]