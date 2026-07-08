# Calculator API

Projeto simples desenvolvido para treinar conceitos básicos de **FastAPI**, **Pytest** e **Docker**.

A ideia do projeto é criar uma API de calculadora com operações matemáticas básicas, usando Python e boas práticas iniciais de organização de código, testes unitários e conteinerização.

## Objetivo do projeto

Este projeto foi criado com fins de estudo, principalmente para praticar:

- Criação de APIs com FastAPI
- Organização básica de projeto em Python
- Programação orientada a objetos com classes
- Testes unitários com Pytest
- Criação de ambiente com Docker
- Execução da aplicação usando Docker Compose

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pytest
- Docker
- Docker Compose

## Funcionalidades

A API possui rotas para as seguintes operações:

- Somar dois números
- Subtrair dois números
- Multiplicar dois números
- Dividir dois números
- Tratar erro de divisão por zero

## Estrutura do projeto

```text
calculadora-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── calculadora.py
│
├── tests/
│   └── test_calculadora.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
Como rodar localmente

Primeiro, crie e ative o ambiente virtual:

python -m venv .venv

No Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Instale as dependências:

pip install -r requirements.txt

Rode a aplicação:

uvicorn app.main:app --reload

Depois acesse:

http://localhost:8000/docs
Como rodar com Docker

Construa e suba o container:

docker compose up --build

Depois acesse:

http://localhost:8000/docs
Como rodar os testes

Para executar os testes localmente:

python -m pytest

Para executar os testes dentro do container:

docker compose exec api python -m pytest
Exemplos de uso

Soma:

http://localhost:8000/somar?a=2&b=3

Resposta esperada:

{
  "resultado": 5
}

Divisão:

http://localhost:8000/dividir?a=10&b=2

Resposta esperada:

{
  "resultado": 5
}
Aprendizados

Durante o desenvolvimento deste projeto, pratiquei a criação de uma API simples com FastAPI, a escrita de testes unitários com Pytest e a conteinerização da aplicação com Docker. Também utilizei Docker Compose para facilitar a execução do projeto em um ambiente padronizado.

Status do projeto

Projeto finalizado como exercício prático de estudos.
