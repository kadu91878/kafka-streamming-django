# Dockerfile

# Use a imagem oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Expõe a porta 8000 para acesso ao Django
EXPOSE 8000

# Comando para rodar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
