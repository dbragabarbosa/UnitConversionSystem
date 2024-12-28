import converter_temperature as converter

def test_celsius_para_fahrenheit():
    assert converter.celsius_para_fahrenheit(0) == 32

def test_fahrenheit_para_kelvin():
    assert round(converter.fahrenheit_para_kelvin(32), 2) == 273.15

def test_kelvin_para_fahrenheit():
    assert round(converter.kelvin_para_fahrenheit(273.15), 2) == 32

def test_celsius_para_kelvin():
    assert converter.celsius_para_kelvin(0) == 273.15

def test_kelvin_para_celsius():
    assert converter.kelvin_para_celsius(273.15) == 0

def test_fahrenheit_para_celsius():
    assert round(converter.fahrenheit_para_celsius(32), 2) == 0

def test_celsius_para_rankine():
    assert round(converter.celsius_para_rankine(0), 2) == 491.67

def test_rankine_para_celsius():
    assert round(converter.rankine_para_celsius(491.67), 2) == 0
