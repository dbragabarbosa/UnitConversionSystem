import converter_velocity as converter

def test_metros_por_segundo_para_quilometros_por_hora():
    assert converter.metros_por_segundo_para_quilometros_por_hora(1) == 3.6

def test_quilometros_por_hora_para_metros_por_segundo():
    assert converter.quilometros_por_hora_para_metros_por_segundo(3.6) == 1.0

def test_milhas_por_hora_para_quilometros_por_hora():
    assert converter.milhas_por_hora_para_quilometros_por_hora(1) == 1.609344

def test_quilometros_por_hora_para_milhas_por_hora():
    assert converter.quilometros_por_hora_para_milhas_por_hora(1.609344) == 1.0

def test_milhas_por_hora_para_pes_por_segundo():
    assert round(converter.milhas_por_hora_para_pes_por_segundo(1), 6) == 1.466667

def test_pes_por_segundo_para_milhas_por_hora():
    assert round(converter.pes_por_segundo_para_milhas_por_hora(1.466667), 6) == 1.0

def test_metros_por_segundo_para_pes_por_segundo():
    assert round(converter.metros_por_segundo_para_pes_por_segundo(1), 6) == 3.28084

def test_pes_por_segundo_para_metros_por_segundo():
    assert round(converter.pes_por_segundo_para_metros_por_segundo(3.28084), 6) == 1.0

def test_milhas_por_hora_para_knot():
    assert round(converter.milhas_por_hora_para_knot(1), 6) == 0.868976

def test_knot_para_milhas_por_hora():
    assert round(converter.knot_para_milhas_por_hora(0.868976), 6) == 1.0

def test_quilometros_por_hora_para_knot():
    assert round(converter.quilometros_por_hora_para_knot(1), 6) == 0.539957

def test_knot_para_quilometros_por_hora():
    assert round(converter.knot_para_quilometros_por_hora(0.539957), 6) == 1.0

def test_metros_por_segundo_para_knot():
    assert round(converter.metros_por_segundo_para_knot(1), 6) == 1.943844

def test_knot_para_metros_por_segundo():
    assert round(converter.knot_para_metros_por_segundo(1.943844), 6) == 1.0

def test_quilometros_por_hora_para_milhas_por_segundo():
    assert round(converter.quilometros_por_hora_para_milhas_por_segundo(3600), 6) == 0.621371

def test_milhas_por_segundo_para_quilometros_por_hora():
    assert round(converter.milhas_por_segundo_para_quilometros_por_hora(0.621371), 6) == 3600

def test_metros_por_segundo_para_milhas_por_hora():
    assert round(converter.metros_por_segundo_para_milhas_por_hora(1), 6) == 2.236936

def test_milhas_por_hora_para_metros_por_segundo():
    assert round(converter.milhas_por_hora_para_metros_por_segundo(2.236936), 6) == 1.0
