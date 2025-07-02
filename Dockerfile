# FRONTEND BUILD
FROM node:20 AS frontend-build
WORKDIR /app
COPY frontend/ .
RUN npm install
RUN npm run build

# BACKEND + FINAL IMAGE
FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .
COPY --from=frontend-build /app/dist /app/static
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
