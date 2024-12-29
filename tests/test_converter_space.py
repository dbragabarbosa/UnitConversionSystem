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

def test_pes_quadrados_para_jardas_quadradas():
    assert converter.pes_quadrados_para_jardas_quadradas(9) == 1

def test_jardas_quadradas_para_pes_quadrados():
    assert converter.jardas_quadradas_para_pes_quadrados(1) == 9

def test_acres_para_jardas_quadradas():
    assert round(converter.acres_para_jardas_quadradas(1), 2) == 4840

def test_jardas_quadradas_para_acres():
    assert round(converter.jardas_quadradas_para_acres(4840), 6) == 1

def test_hectares_para_jardas_quadradas():
    assert round(converter.hectares_para_jardas_quadradas(1), 6) == 11959.900463

def test_jardas_quadradas_para_hectares():
    assert round(converter.jardas_quadradas_para_hectares(11959.900463), 6) == 1

def test_milhas_quadradas_para_hectares():
    assert converter.milhas_quadradas_para_hectares(1) == 258.998811

def test_hectares_para_milhas_quadradas():
    assert round(converter.hectares_para_milhas_quadradas(258.998811), 6) == 1

def test_milhas_quadradas_para_acres():
    assert converter.milhas_quadradas_para_acres(1) == 640

def test_acres_para_milhas_quadradas():
    assert converter.acres_para_milhas_quadradas(640) == 1

def test_metros_quadrados_para_jardas_quadradas():
    assert round(converter.metros_quadrados_para_jardas_quadradas(1), 6) == 1.195990

def test_jardas_quadradas_para_metros_quadrados():
    assert round(converter.jardas_quadradas_para_metros_quadrados(1.195990), 6) == 1
