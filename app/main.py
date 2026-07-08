from fastapi import FastAPI
from app.calculadora import Calculadora

app = FastAPI()

calculadora = Calculadora()
#cria um objeto da classe Calculadora()

@app.get("/")
def home():
    return {"API da calculadora funcionando"}

@app.get("/somar")
def rota_somar(a: float, b:float):
    resultado = calculadora.somar(a, b)
    return {"resultado": resultado}

@app.get("/subtrair")
def rota_subtrair(a: float, b: float):
    resultado = calculadora.subtrair(a,b)
    return {"resultado": resultado}

@app.get("/multiplicar")
def rota_multiplicacao(a: float, b: float):
    resultado = calculadora.multiplicacao(a, b)
    return {"resultado": resultado}

@app.get("/dividir")
def rota_dividir(a: float, b:float):
    resultado = calculadora.dividir(a,b)
    return {"resultado": resultado}
