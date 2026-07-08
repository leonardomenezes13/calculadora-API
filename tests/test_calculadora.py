import pytest
from app.calculadora import Calculadora

def test_somar():
    calculadora = Calculadora()

    resultado = calculadora.somar(2,3)

    assert resultado == 5

def test_subtrair():
    calculadora = Calculadora()

    resultado = calculadora.subtrair(10,4)

    assert resultado == 6

def test_multiplicar():
    calculadora  = Calculadora()

    resultado = calculadora.multiplicar(5,5)

    assert resultado == 25

def test_dividir():
    calculadora = Calculadora()

    resultado = calculadora.dividir(6,3)

    assert resultado == 2

def test_divisao_zero():
    calc = Calculadora()

    with pytest.raises(ValueError):
        calc.dividir(10,0)