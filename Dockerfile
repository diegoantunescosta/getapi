# Use uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do seu projeto para o diretório de trabalho
COPY . .

# Instala as dependências
RUN pip install -r requirements.txt

# Define o comando para rodar a aplicação
CMD ["python", "app.py"]
