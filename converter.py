# Funções de conversão para comprimento
def metros_para_quilometros(metros):
    return metros / 1000

def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

# Funções de conversão para peso
def quilogramas_para_gramas(quilogramas):
    return quilogramas * 1000

def gramas_para_libras(gramas):
    return gramas * 0.00220462

# Funções de conversão para temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
