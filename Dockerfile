FROM python:3.12-slim

# зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# копируем код проекта
COPY app ./app

# копируем alembic
COPY alembic ./alembic
COPY alembic.ini .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]