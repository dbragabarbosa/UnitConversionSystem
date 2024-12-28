import converter_time as converter

def test_segundos_para_minutos():
    assert converter.segundos_para_minutos(120) == 2

def test_minutos_para_segundos():
    assert converter.minutos_para_segundos(2) == 120

def test_minutos_para_horas():
    assert converter.minutos_para_horas(120) == 2

def test_horas_para_minutos():
    assert converter.horas_para_minutos(2) == 120

def test_horas_para_dias():
    assert converter.horas_para_dias(48) == 2

def test_dias_para_horas():
    assert converter.dias_para_horas(2) == 48

def test_segundos_para_horas():
    assert converter.segundos_para_horas(7200) == 2

def test_horas_para_segundos():
    assert converter.horas_para_segundos(2) == 7200

def test_dias_para_minutos():
    assert converter.dias_para_minutos(2) == 2880

def test_minutos_para_dias():
    assert converter.minutos_para_dias(2880) == 2

def test_dias_para_segundos():
    assert converter.dias_para_segundos(2) == 172800

def test_segundos_para_dias():
    assert converter.segundos_para_dias(172800) == 2
