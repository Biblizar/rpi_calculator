# Dockerfile

FROM python:3.11-slim

# Défine Workdir 
WORKDIR /app

# Copy dependencies file first to optimize Docker cache & Install dependencies 
COPY api/requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir -r /api/requirements.txt

# Copy API files
COPY ./api /app/api


# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]