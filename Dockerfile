FROM node:18-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json ./
RUN apk add --no-cache python3 make g++   # dipendenze build se servono
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ ./backend
COPY --from=frontend-build /app/frontend/dist ./frontend
RUN mkdir -p public/downloads
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
