import pytest 
from fatorial import fatorial

@pytest.mark.parametrize("factor, expected", [(3, 6),(4, 24),(5, 120),(6, 720)])

def test_factor(factor, expected):
    assert fatorial(factor) == expected
