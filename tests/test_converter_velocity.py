import converter_velocity as converter

def test_mps_para_kmh():
    assert converter.mps_para_kmh(1) == 3.6

def test_kmh_para_mps():
    assert converter.kmh_para_mps(3.6) == 1.0

def test_mps_para_mph():
    assert converter.mps_para_mph(1) == 2.23694

def test_mph_para_mps():
    assert converter.mph_para_mps(2.23694) == 1.0

def test_kmh_para_mph():
    assert converter.kmh_para_mph(1) == 0.621371

def test_mph_para_kmh():
    assert converter.mph_para_kmh(0.621371) == 1.0

def test_kmh_para_knots():
    assert converter.kmh_para_knots(1) == 0.539957

def test_knots_para_kmh():
    assert converter.knots_para_kmh(0.539957) == 1.0

def test_mph_para_fts():
    assert converter.mph_para_fts(1) == 1.46667

def test_fts_para_mph():
    assert converter.fts_para_mph(1.46667) == 1.0

def test_mps_para_fts():
    assert converter.mps_para_fts(1) == 3.28084

def test_fts_para_mps():
    assert converter.fts_para_mps(3.28084) == 1.0

def test_knots_para_mps():
    assert converter.knots_para_mps(1) == 0.514444

def test_mps_para_knots():
    assert converter.mps_para_knots(0.514444) == 1.0

def test_knots_para_mph():
    assert converter.knots_para_mph(1) == 1.15078

def test_mph_para_knots():
    assert converter.mph_para_knots(1.15078) == 1.0

def test_kmh_para_cmps():
    assert converter.kmh_para_cmps(1) == 27.7778

def test_cmps_para_kmh():
    assert converter.cmps_para_kmh(27.7778) == 1.0

def test_kmh_para_mmin():
    assert converter.kmh_para_mmin(1) == 16.6667

def test_mmin_para_kmh():
    assert converter.mmin_para_kmh(16.6667) == 1.0
