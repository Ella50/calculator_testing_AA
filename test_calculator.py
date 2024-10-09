import pytest
from calculator import sum, sub, mult, div

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, 2) == 1
    assert sum(-1, -2) == -3
    assert sum(0, 0) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(-1, 2) == -3
    assert sub(-1, -2) == 1
    assert sub(0, 0) == 0

def test_mult():
    assert mult(1, 2) == 2
    assert mult(-1, 2) == -2
    assert mult(-1, -3) == 3
    assert mult(0, 2) == 0

def test_div():
    assert div(6, 2) == 3
    assert div(-4, 2) == -2
    assert div(-2, -2) == 1
    assert div(0, 2) == 0
    assert div(3, 0) == "Error: Division by zero"
    

# def test_div_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(3, 0)