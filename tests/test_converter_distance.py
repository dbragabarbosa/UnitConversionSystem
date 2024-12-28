import converter_distance as converter

def test_metros_para_quilometros():
    assert converter.metros_para_quilometros(1000) == 1

def test_quilometros_para_milhas():
    assert converter.quilometros_para_milhas(1) == 0.621371

def test_jardas_para_metros():
    assert converter.jardas_para_metros(1) == 0.9144

def test_milhas_para_metros():
    assert converter.milhas_para_metros(1) == 1609.34

def test_polegadas_para_centimetros():
    assert converter.polegadas_para_centimetros(1) == 2.54

def test_centimetros_para_polegadas():
    assert converter.centimetros_para_polegadas(2.54) == 1

def test_metros_para_polegadas():
    assert converter.metros_para_polegadas(1) == 39.3701

def test_polegadas_para_metros():
    assert converter.polegadas_para_metros(39.3701) == 1
