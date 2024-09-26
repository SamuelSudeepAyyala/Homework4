''' My Calculator Test with Calculator emcapsulation'''
from calculator import Calculator
import pytest

def test_add():
    result = Calculator.add(2,3)
    assert  result == 5

def test_subtract():
    assert Calculator.subtract(5,3) == 2

def test_multiply():
    assert Calculator.multiply(4,5) == 20

def test_divide():
    assert Calculator.divide(10,2) == 5

def test_divideByZero():
    with pytest.raises(ValueError):
        Calculator.divide(10,0)