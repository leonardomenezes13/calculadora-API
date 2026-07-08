FROM python:3.12-slim 
#usa uma imagem pronta do python

WORKDIR /app
#cria e entra numa pasta chamada /app dentro do container

COPY requirements.txt .
#copia o arquivo requirements.txt para dentro do container

RUN pip install --no-cache-dir -r requirements.txt
#instala as bibliotecas do projeto: FastAPI, Uvicorn, Pytest

COPY . .
#copia todo o projeto para dentro do container

CMD ["uvicorn" , "app.main:app" , "--host", "0.0.0.0" , "--port", "8000"]
#comando que roda a API quando o container iniciar