FROM python:3.11-slim

ARG OUTPUT_PATH=/data/output

ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1 \
    OUTPUT_PATH=$OUTPUT_PATH

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    addgroup --system app_group && \
    adduser --system --group app_user && \
    mkdir -p $OUTPUT_PATH && \
    chown -R app_user:app_user $OUTPUT_PATH

COPY . .

USER app_user

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

COPY requirements.txt .
