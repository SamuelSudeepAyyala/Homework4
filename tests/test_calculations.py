''' My Calculator History Test '''
from decimal import Decimal
import pytest

from calculator.Calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def make_calculations():
    """cleaning the history and adding sample make_calculations"""
    calculations.delete_history()

    calculations.add_history(Calculation(Decimal('2'), Decimal('3'), add))
    calculations.add_history(Calculation(Decimal('10'), Decimal('3'), subtract))
    calculations.add_history(Calculation(Decimal('5'), Decimal('3'), multiply))
    calculations.add_history(Calculation(Decimal('15'), Decimal('3'), divide))

def test_addcalculation():
    """Testing the addition of history"""
    add_obj = Calculation(Decimal('3'),Decimal('3'), add)
    calculations.add_history(add_obj)
    assert calculations.get_latest_history() == add_obj

def test_gethistory(make_calculations):
    """Testing the addition of history"""
    history = calculations.print_history()
    assert len(history) == 4

def test_clearhistory():
    """Testing the addition of history"""
    calculations.delete_history()
    assert len(calculations.print_history()) == 0

def test_getlatest(make_calculations):
    """Testing the addition of history"""
    latest = calculations.get_latest_history()
    assert latest.a == Decimal('15') and latest.b == Decimal('3')

def test_getlatestafterclear():
    """Testing the addition of history"""
    calculations.delete_history()
    assert calculations.get_latest_history() is None

def test_findbyoperation(make_calculations):
    """Testing the addition of history"""
    getbyadd_operation = calculations.get_with_operation("add")
    assert len(getbyadd_operation) == 1
    getbymultiply_operation = calculations.get_with_operation("multiply")
    assert len(getbymultiply_operation) == 1
