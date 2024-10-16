# Dockerfile

FROM python:3.11-slim

# Défine Workdir 
WORKDIR /api

# Copy API files
COPY api/ ./api

# Install dependencies 
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]