from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.calculations import calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    """
    This is a class is to have static methods for performing the arithmetic operations like a calculator. We use History store mechanism to have all the calculations made.
    
    Methods Initialised
    -------------------

    do_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
    This method performs the operation specified for two decimals by calling create method and stores the calculation to the history.

    add(a: Decimal, b: Decimal) -> Decimal:

    subtract(a: Decimal, b: Decimal) -> Decimal:

    multiply(a: Decimal, b:Decimal) -> Decimal:

    divide(a: Decimal, b:Decimal) -> Decimal:

    All the above methods with perform arithmetic operations on two decimals and stores them in history.
    """
    @staticmethod
    def do_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        '''
        This method performs the specified arithmetic operation on two decimal numbers. The operation that is performed is passed as callable function (add, subtract, multiply, divide). The calculation is stored in history after the result is stored in history.

        Parameters
        ----------
        a: Decimal, b: Decimal
        The numbers in the operation.
        operation : Callable[[Decimal, Decimal], Decimal]
        The operation that needs to be performed on the above number 

        Returns
        -------
        The result of the calculation performed.
        '''
        calculation = Calculation.createCalculation(a, b, operation)
        calculations.add_history(calculation)
        return calculation.calculate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        This method adds two decimal numbers and stores the calculations to the history.

        Parameters
        ----------
        a: Decimal, b:Decimal - numbers to perform addition operation

        Returns
        -------
        The result of addition of two numbers
        """
        return Calculator.do_operation(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        This method subtracts the number a from the number b and stores the operation in history.

        Parameters
        ----------
        a: Decimal, b:Decimal - numbers to perform subtraction operation

        Returns
        -------
        The result of difference between a and b
        """
        return Calculator.do_operation(a,b,subtract)

    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        """
        This method returns the product of two decimal numbers a and b. Stores the operation in history.

        Parameters
        ----------
        a: Decimal, b:Decimal - numbers to perform multiplication operation

        Returns
        -------
        The result of product between a and b
        """
        return Calculator.do_operation(a,b,multiply)
    
    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        """
        This method returns the division of two decimal numbers a and b. Stores the operation in history. This method raises an exception when divided by Zero.

        Parameters
        ----------
        a: Decimal, b:Decimal - numbers to perform division operation

        Returns
        -------
        The result of division with b by a.
        """
        return Calculator.do_operation(a,b,divide)
