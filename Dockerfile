FROM python:3.11-slim
WORKDIR /app
COPY backend requirements.txt ./
RUN pip install -r requirements.txt
COPY frontend/ /app/frontend/
COPY public/ /app/public/
COPY backend/ /app/backend/
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
