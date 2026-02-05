import pytest
from src.math_operations import subtract

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_mixed():
    assert subtract(-5, 3) == -8

def test_subtract_float():
    assert subtract(5.5, 3.1) == pytest.approx(2.4)
