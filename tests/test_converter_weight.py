import converter_weight as converter

# Testes para peso
def test_quilogramas_para_gramas():
    assert converter.quilogramas_para_gramas(1) == 1000

def test_gramas_para_libras():
    assert round(converter.gramas_para_libras(1000), 5) == 2.20462

def test_oncas_para_gramas():
    assert round(converter.oncas_para_gramas(1), 4) == 28.3495

def test_libras_para_quilogramas():
    assert round(converter.libras_para_quilogramas(1), 6) == 0.453592

def test_quilogramas_para_libras():
    assert round(converter.quilogramas_para_libras(1), 5) == 2.20462

def test_libras_para_gramas():
    assert round(converter.libras_para_gramas(1), 3) == 453.592

def test_gramas_para_quilogramas():
    assert converter.gramas_para_quilogramas(1000) == 1

def test_oncas_para_libras():
    assert round(converter.oncas_para_libras(16), 1) == 1

def test_libras_para_oncas():
    assert converter.libras_para_oncas(1) == 16
