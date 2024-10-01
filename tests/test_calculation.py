"""
This module consists of the code representing the unit tests for the 'Calculation' class, testing various methods initialised in the class using pytest framework.
these tests will ensure that the methods in the 'calculation' class will behave correctly with the different types of inputs provided and exception cases like dividebyZero.
"""

from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,divide

# The pytest.mark.parametrize is a decorator used to run the same test function multiple times with different sets of input parameters and expected outputs. This will help to ensure that
# Calculation class can handle various operations without duplicating the code.

# Parameters
# ----------
# a -> The first operand in the operation which is a Decimal.
# b -> The second operand in the operation which is a Decimal.
# operation -> The operation that needs to be performed like add, subtract, multiply and divide
# expected -> The expected output after the operation is performed which will be represented as a Decimal.

def test_calculate(a, b, operation, expected):
    '''Test the 'calculate' method from the 'calculation' class with various arithmetic operations. This test will check if  correct result is being returned for different operations
    using the parameters passed.
    Parameters passed for test cases
    --------------------------------
    
    a and b [ Decimal ] -> are the operands that are decimals on which the operations are needed to be performed.
    operation [ Callable[[Decimal, Decimal], Decimal] ] ->  The arithmetic operation that needs to be performed.
    expected [ Decimal ] -> The expected result of the operation performed.
    2, 3, add, 5
    5, 3, subtract, 2
    15, 3, divide, 5
    4, 3, multiply, 12
    3, 3, add, 6
    
    Raises
    ------
    - AssertionError
        It raises an assertion error if the return is not equal to expected.
    '''
    obj = Calculation(a, b, operation)
    assert obj.calculate() == expected, f"Operation {operation.__name__} has been failed!!"

def test_repr():
    """ 
    Testing the method for string representation ('__stringify__') of the Calculation object. The test will ensure that the string representation of the instance will correctly
    reflects the operands and the operation. For example if the object is created for '10 and 5'. It should return the string in the format "Calculation(10, 5, add)"
    
    Test Case:
        - Inputs: 10 (a), 5 (b), add (operation)
        - Expected output string : "Calculation(10, 5, add)"

    Raises
    ------
    AssertionError
        If the return string doesnt match the expected output.
    """
    obj = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert obj.__stringify__() == expected_repr, f"String representation failed! Expected {expected_repr}, returned {obj.__stringify__()}."


def test_dividebyzero():
    """
    This method is to test the behavior of the Calculation class when there is a division occured by zero.

    While doing the arithmetic operations and in the division methods while doing a division by zero it should raise a 'ValueError'
    to prevent the invalid arithmetic operation to perform. This test case will ensure the correct exception is raised or not with an appropriate error message.
    
    Test Case:
        - Inputs: 5 (a), 0 (b), divide (operation)
        - Expected behavior: A `ValueError` is raised with the message "Cannot divide by zero"

    Raises
    ------
    ValueError
        If division by zero is attempted, with the error message "Cannot divide by zero".
    """
    obj = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        obj.calculate()
