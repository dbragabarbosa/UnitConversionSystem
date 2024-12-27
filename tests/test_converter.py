import converter

# Testes para comprimento
def test_metros_para_quilometros():
    assert converter.metros_para_quilometros(1000) == 1

def test_quilometros_para_milhas():
    assert converter.quilometros_para_milhas(1) == 0.621371

def test_jardas_para_metros():
    assert converter.jardas_para_metros(1) == 0.9144

def test_milhas_para_metros():
    assert converter.milhas_para_metros(1) == 1609.34

# Testes para peso
def test_quilogramas_para_gramas():
    assert converter.quilogramas_para_gramas(1) == 1000

def test_gramas_para_libras():
    assert converter.gramas_para_libras(1000) == 2.20462

def test_oncas_para_gramas():
    assert round(converter.oncas_para_gramas(1), 4) == 28.3495

def test_libras_para_quilogramas():
    assert round(converter.libras_para_quilogramas(1), 6) == 0.453592

# Testes para temperatura
def test_celsius_para_fahrenheit():
    assert converter.celsius_para_fahrenheit(0) == 32

def test_fahrenheit_para_kelvin():
    assert round(converter.fahrenheit_para_kelvin(32), 2) == 273.15

def test_kelvin_para_fahrenheit():
    assert round(converter.kelvin_para_fahrenheit(273.15), 2) == 32