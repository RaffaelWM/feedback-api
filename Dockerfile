# Usa imagem oficial Python slim
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponha a porta que o uvicorn vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
