import converter_space as converter

def test_metros_quadrados_para_quilometros_quadrados():
    assert converter.metros_quadrados_para_quilometros_quadrados(1_000_000) == 1

def test_quilometros_quadrados_para_metros_quadrados():
    assert converter.quilometros_quadrados_para_metros_quadrados(1) == 1_000_000

def test_acres_para_metros_quadrados():
    assert round(converter.acres_para_metros_quadrados(1), 2) == 4046.86

def test_metros_quadrados_para_acres():
    assert round(converter.metros_quadrados_para_acres(4046.86), 2) == 1

def test_hectares_para_metros_quadrados():
    assert converter.hectares_para_metros_quadrados(1) == 10_000

def test_metros_quadrados_para_hectares():
    assert converter.metros_quadrados_para_hectares(10_000) == 1

def test_acres_para_hectares():
    assert round(converter.acres_para_hectares(1), 6) == 0.404686

def test_hectares_para_acres():
    assert round(converter.hectares_para_acres(1), 6) == 2.471054

def test_quilometros_quadrados_para_hectares():
    assert converter.quilometros_quadrados_para_hectares(1) == 100

def test_hectares_para_quilometros_quadrados():
    assert converter.hectares_para_quilometros_quadrados(100) == 1

def test_acres_para_quilometros_quadrados():
    assert round(converter.acres_para_quilometros_quadrados(1), 8) == 0.00404686

def test_quilometros_quadrados_para_acres():
    assert round(converter.quilometros_quadrados_para_acres(1), 6) == 247.105381
