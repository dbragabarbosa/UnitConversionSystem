import converter_distance as converter

def test_metros_para_quilometros():
    assert converter.metros_para_quilometros(1000) == 1

def test_quilometros_para_metros():
    assert converter.quilometros_para_metros(1) == 1000

def test_quilometros_para_milhas():
    assert converter.quilometros_para_milhas(1) == 0.621371

def test_milhas_para_quilometros():
    assert round(converter.milhas_para_quilometros(1), 6) == 1.609344

def test_jardas_para_metros():
    assert converter.jardas_para_metros(1) == 0.9144

def test_metros_para_jardas():
    assert round(converter.metros_para_jardas(1), 6) == 1.093613

def test_jardas_para_quilometros():
    assert round(converter.jardas_para_quilometros(1093.613), 6) == 1

def test_quilometros_para_jardas():
    assert round(converter.quilometros_para_jardas(1), 3) == 1093.613

def test_milhas_para_metros():
    assert converter.milhas_para_metros(1) == 1609.34

def test_metros_para_milhas():
    assert round(converter.metros_para_milhas(1609.34), 6) == 1

def test_polegadas_para_centimetros():
    assert converter.polegadas_para_centimetros(1) == 2.54

def test_centimetros_para_polegadas():
    assert converter.centimetros_para_polegadas(2.54) == 1

def test_metros_para_polegadas():
    assert round(converter.metros_para_polegadas(1), 4) == 39.3701

def test_polegadas_para_metros():
    assert round(converter.polegadas_para_metros(39.3701), 4) == 1

def test_polegadas_para_jardas():
    assert round(converter.polegadas_para_jardas(36), 6) == 0.999999

def test_jardas_para_polegadas():
    assert converter.jardas_para_polegadas(1) == 36.00001944

def test_centimetros_para_metros():
    assert converter.centimetros_para_metros(100) == 1

def test_metros_para_centimetros():
    assert converter.metros_para_centimetros(1) == 100

def test_milhas_para_polegadas():
    assert round(converter.milhas_para_polegadas(1), 2) == 63359.88

def test_polegadas_para_milhas():
    assert round(converter.polegadas_para_milhas(63360), 6) == 1.000002

def test_quilometros_para_centimetros():
    assert converter.quilometros_para_centimetros(1) == 100000

def test_centimetros_para_quilometros():
    assert converter.centimetros_para_quilometros(100000) == 1

def test_milhas_para_jardas():
    assert converter.milhas_para_jardas(1) == 1759.9956255468067

def test_jardas_para_milhas():
    assert converter.jardas_para_milhas(1760) == 1.0000024854909466

