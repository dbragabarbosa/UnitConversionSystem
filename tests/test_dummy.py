# test_dummy.py
from main import somar
from main import subtrair
from main import multiplicar

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(3, 2) == 1

def test_multiplicar():
    assert multiplicar(2, 3) == 6