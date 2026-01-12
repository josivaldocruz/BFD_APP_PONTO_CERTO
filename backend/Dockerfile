FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements e instalar
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copiar o código da aplicação
COPY . /app

# criar diretório para arquivos estáticos e media
RUN mkdir -p /app/staticfiles /app/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
