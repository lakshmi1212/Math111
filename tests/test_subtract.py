import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (7.5, 2.5, 5.0),
    (-3, 3, -6),
    (1000000, 1, 999999),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
