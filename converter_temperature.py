# Funções de conversão para temperatura
def celsius_para_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    return result

def fahrenheit_para_kelvin(fahrenheit):
    result = (fahrenheit - 32) * 5/9 + 273.15
    return result

def kelvin_para_fahrenheit(kelvin):
    result = (kelvin - 273.15) * 9/5 + 32
    return result

def celsius_para_kelvin(celsius):
    result = celsius + 273.15
    return result

def kelvin_para_celsius(kelvin):
    result = kelvin - 273.15
    return result

def fahrenheit_para_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return result

def celsius_para_rankine(celsius):
    result = (celsius + 273.15) * 9/5
    return result

def rankine_para_celsius(rankine):
    result = (rankine - 491.67) * 5/9
    return result
