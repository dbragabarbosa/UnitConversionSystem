import converter_volume as converter

def test_litros_para_mililitros():
    assert converter.litros_para_mililitros(1) == 1000

def test_mililitros_para_litros():
    assert converter.mililitros_para_litros(1000) == 1

def test_litros_para_galoes():
    assert round(converter.litros_para_galoes(1), 6) == 0.264172

def test_galoes_para_litros():
    assert round(converter.galoes_para_litros(1), 6) == 3.785413

def test_metros_cubicos_para_litros():
    assert converter.metros_cubicos_para_litros(1) == 1000

def test_litros_para_metros_cubicos():
    assert converter.litros_para_metros_cubicos(1000) == 1

def test_metros_cubicos_para_galoes():
    assert round(converter.metros_cubicos_para_galoes(1), 3) == 264.172

def test_galoes_para_metros_cubicos():
    assert round(converter.galoes_para_metros_cubicos(1), 6) == 0.003785

def test_mililitros_para_galoes():
    assert round(converter.mililitros_para_galoes(3785.41), 6) == 1.0

def test_galoes_para_mililitros():
    assert round(converter.galoes_para_mililitros(1), 2) == 3785.41

def test_litros_para_pintas():
    assert round(converter.litros_para_pintas(1), 5) == 2.11338

def test_pintas_para_litros():
    assert round(converter.pintas_para_litros(1), 6) == 0.473176
