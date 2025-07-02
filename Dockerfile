FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/
COPY public/ /app/public/
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
