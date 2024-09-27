''' My Calculator History Test '''
from decimal import Decimal
import pytest

from calculator.Calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def make_calculations():
    """This fixture is to clean the existing history and add some sample calculations. This will be executed before each test that needs it."""

    calculations.delete_history() # clears the existing history

    # Adds sample calculations to the history.
    calculations.add_history(Calculation(Decimal('2'), Decimal('3'), add))
    calculations.add_history(Calculation(Decimal('10'), Decimal('3'), subtract))
    calculations.add_history(Calculation(Decimal('5'), Decimal('3'), multiply))
    calculations.add_history(Calculation(Decimal('15'), Decimal('3'), divide))

def test_addcalculation():
    """
    Testing to add a calculation to history.
    Verifies whether the calculation is successfully added and can be retrieved from history.
    """
    # Create a new addition calculation
    add_obj = Calculation(Decimal('3'),Decimal('3'), add)
    # Add the calculation to history
    calculations.add_history(add_obj)
    # Assert the latest calculation from history should be the one we have added now.
    assert calculations.get_latest_history() == add_obj

def test_gethistory(make_calculations):
    """
    Test for getting the entire calculation history. Verifies that the correct count of entries are stored.
    """
    # Retrieve the calculation history and check its length
    history = calculations.print_history()
    assert len(history) == 4

def test_clearhistory():
    """
    Test for clearing the calculation history. Verifies that all entries are successfully deleted.
    """
    calculations.delete_history()
    assert len(calculations.print_history()) == 0

def test_getlatest(make_calculations):
    """
    Test for retrieving the latest calculation in history. Verify that the correct latest entry is returned.
    """
    # Retrieve the latest calculation
    latest = calculations.get_latest_history()
    # Assert the latest calculation is the last one added
    assert latest.a == Decimal('15') and latest.b == Decimal('3')

def test_getlatestafterclear():
    """
    Test for retrieving the latest calculation after clearing history. Asserts that None is returned when no calculations are in history.
    """
    # Clear the history
    calculations.delete_history()
    # Asserts the latest history is equal to None as the history is empty.
    assert calculations.get_latest_history() is None

def test_findbyoperation(make_calculations):
    """
    Test for finding calculations by operation. Verifies that calculations with a specific operation can be retrieved.
    """

    # Find calculations by 'add' operation that are inserted in the history and assert only one result is found
    getbyadd_operation = calculations.get_with_operation("add")
    assert len(getbyadd_operation) == 1
    # Find calculations by 'multiply' operation that are inserted in the history and assert only one result is found
    getbymultiply_operation = calculations.get_with_operation("multiply")
    assert len(getbymultiply_operation) == 1
