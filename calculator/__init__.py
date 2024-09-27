from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.calculationhistory import Calculationhistory
from decimal import Decimal
from typing import Callable

class Calculator:

    @staticmethod
    def do_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        calculation = Calculation.createCalculation(a, b, operation)
        Calculationhistory.add_history(calculation)
        return calculation.calculate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.do_operation(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.do_operation(a,b,subtract)

    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        return Calculator.do_operation(a,b,multiply)
    
    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        return Calculator.do_operation(a,b,divide)
