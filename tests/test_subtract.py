import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (200, 100, 100),
    (-5, 5, -10),
    (5, -5, 10),
    (2.5, 1.5, 1.0),
    (-1.5, 1.5, -3.0)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
