# BFD_APP_PONTO_CERTO

# Ponto Certo - PDV

Sistema de Ponto de Venda desenvolvido em Django e PostgreSQL.

## Requisitos

- Python 3.10+
- PostgreSQL
- Docker (opcional)

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url>
   cd ponto_certo
Crie um ambiente virtual e ative:

## 2. Crie um ambiente virtual e ative:

bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

## 3. Instale as dependências:

bash
pip install -r requirements.txt

## 4 .Configure o banco de dados:

Com Docker: docker-compose up -d

Ou instale e configure o PostgreSQL manualmente.

## 5. Crie um arquivo

.env na raiz do projeto com as variáveis de ambiente (veja .env.example).

## 6. Execute as migrações:

bash
cd backend
python manage.py migrate


## 7. Crie um superusuário:

bash
python manage.py createsuperuser


## 8. Execute o servidor:

bash
python manage.py runserver


## 9. Acesse http://localhost:8000 e faça login.

