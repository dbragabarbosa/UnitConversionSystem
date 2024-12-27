import converter_temperature as converter

# Testes para temperatura
def test_celsius_para_fahrenheit():
    assert converter.celsius_para_fahrenheit(0) == 32

def test_fahrenheit_para_kelvin():
    assert round(converter.fahrenheit_para_kelvin(32), 2) == 273.15

def test_kelvin_para_fahrenheit():
    assert round(converter.kelvin_para_fahrenheit(273.15), 2) == 32