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

def test_acres_para_jardas_quadradas():
    assert round(converter.acres_para_jardas_quadradas(1), 2) == 4840

def test_jardas_quadradas_para_acres():
    assert round(converter.jardas_quadradas_para_acres(4840), 6) == 1

def test_hectares_para_jardas_quadradas():
    assert round(converter.hectares_para_jardas_quadradas(1), 6) == 11959.900463

def test_jardas_quadradas_para_hectares():
    assert round(converter.jardas_quadradas_para_hectares(11959.900463), 6) == 1

def test_milhas_quadradas_para_acres():
    assert converter.milhas_quadradas_para_acres(1) == 640

def test_acres_para_milhas_quadradas():
    assert converter.acres_para_milhas_quadradas(640) == 1

def test_metros_quadrados_para_jardas_quadradas():
    assert round(converter.metros_quadrados_para_jardas_quadradas(1), 6) == 1.195991

def test_jardas_quadradas_para_metros_quadrados():
    assert round(converter.jardas_quadradas_para_metros_quadrados(1.195990), 6) == 1

def test_pes_quadrados_para_metros_quadrados():
    assert round(converter.pes_quadrados_para_metros_quadrados(1), 6) == 0.092903

def test_metros_quadrados_para_pes_quadrados():
    assert round(converter.metros_quadrados_para_pes_quadrados(1), 6) == 10.76391

def test_milhas_quadradas_para_quilometros_quadrados():
    assert round(converter.milhas_quadradas_para_quilometros_quadrados(1), 5) == 2.58999

def test_quilometros_quadrados_para_milhas_quadradas():
    assert round(converter.quilometros_quadrados_para_milhas_quadradas(1), 6) == 0.386102

def test_polegadas_quadradas_para_centimetros_quadrados():
    assert round(converter.polegadas_quadradas_para_centimetros_quadrados(1), 4) == 6.4516

def test_centimetros_quadrados_para_polegadas_quadradas():
    assert round(converter.centimetros_quadrados_para_polegadas_quadradas(6.4516), 6) == 1

def test_metros_quadrados_para_milimetros_quadrados():
    assert converter.metros_quadrados_para_milimetros_quadrados(1) == 1_000_000

def test_milimetros_quadrados_para_metros_quadrados():
    assert converter.milimetros_quadrados_para_metros_quadrados(1_000_000) == 1

def test_metros_quadrados_para_centimetros_quadrados():
    assert converter.metros_quadrados_para_centimetros_quadrados(1) == 10_000

def test_centimetros_quadrados_para_metros_quadrados():
    assert converter.centimetros_quadrados_para_metros_quadrados(10_000) == 1
