from converter import (
    metros_para_quilometros,
    quilometros_para_milhas,
    quilogramas_para_gramas,
    gramas_para_libras,
    celsius_para_fahrenheit,
    fahrenheit_para_kelvin,
)

# Testes para comprimento
def test_metros_para_quilometros():
    assert metros_para_quilometros(1000) == 1

def test_quilometros_para_milhas():
    assert quilometros_para_milhas(1) == 0.621371

# Testes para peso
def test_quilogramas_para_gramas():
    assert quilogramas_para_gramas(1) == 1000

def test_gramas_para_libras():
    assert gramas_para_libras(1000) == 2.20462

# Testes para temperatura
def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32

def test_fahrenheit_para_kelvin():
    assert round(fahrenheit_para_kelvin(32), 2) == 273.15
