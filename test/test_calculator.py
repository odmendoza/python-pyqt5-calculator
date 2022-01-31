import pytest

from src.util import calculator

@pytest.mark.parametrize(
    ['a', 'b', 'output'],
    [(6, 2, 8),
     (8, 2, 10)
     ]
    )
def test_add(a, b, output):
    assert calculator.add(a, b) == output

@pytest.mark.parametrize(
    ['a', 'b', 'output'],
    [(6, 2, 4),
     (8, 2, 6)
     ]
    )
def test_substract(a, b, output):
    assert calculator.substract(a, b) == output

@pytest.mark.parametrize(
    ['a', 'b', 'output'],
    [(6, 2, 12),
     (8, 2, 16)
     ]
    )
def test_multiply(a, b, output):
    assert calculator.multiply(a, b) == output

@pytest.mark.parametrize(
    ['a', 'b', 'output'],
    [(6, 2, 3),
     (8, 2, 4),
     (8, 0, None)
     ]
    )
def test_divide(a, b, output):
    assert calculator.divide(a, b) == output

@pytest.mark.parametrize(
    ['a','output'],
    [('1', True),
     ('a', False)
     ]
    )
def test_is_a_natural_number(a,output):
    assert calculator.is_a_natural_number(a) == output
