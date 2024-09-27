"""
Module docstring
"""

from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,subtract,multiply,divide


@pytest.mark.parametrize("num1, num2, operation, expected",
[
    (Decimal('2'), Decimal('3'), add, Decimal('5')),
    (Decimal('5'), Decimal('3'), subtract, Decimal('2')),
    (Decimal('15'), Decimal('3'), divide, Decimal('5')),
    (Decimal('4'), Decimal('3'), multiply, Decimal('12')),
    (Decimal('3'), Decimal('3'), add, Decimal('6'))
])

def test_calculate(num1, num2, operation, expected):
    ''' Text '''
    obj = Calculation(num1, num2, operation)
    assert obj.calculate() == expected, f"Operation {operation.__name__} has been failed!!"

def test_repr():
    """ Text """
    obj = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert obj.__stringify__() == expected_repr


def test_dividebyzero():
    ''' Text '''
    obj = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Division By Zero is not allowed!"):
        obj.calculate()
