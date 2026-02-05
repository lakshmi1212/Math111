import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (2.5, 1.5, 1.0),
    (3, 5, -2)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
