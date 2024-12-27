import converter_weight as converter

# Testes para peso
def test_quilogramas_para_gramas():
    assert converter.quilogramas_para_gramas(1) == 1000

def test_gramas_para_libras():
    assert converter.gramas_para_libras(1000) == 2.20462

def test_oncas_para_gramas():
    assert round(converter.oncas_para_gramas(1), 4) == 28.3495

def test_libras_para_quilogramas():
    assert round(converter.libras_para_quilogramas(1), 6) == 0.453592