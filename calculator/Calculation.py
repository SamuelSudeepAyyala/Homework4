from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """
    This class is used to represent the arithmetic calculations which involves two decimal numbers and a operation.
    
    ***Encapsulation***:
    The 'Calculation' class does the encapsulation of the data i.e., a and b operands and the operation passed as a Callable function and the methods that operates on the data.
    This design will restrict the direct access of internal attribute by making controlled interactions using the methods. Using this method users can perform calculations without 
    the need to understand the internal logic of how the calcualtions are happening, So we can ensure data integrity and reduce complexity in class usage.

    """
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        '''
        Constructor for all the necessary attributes for Calculator object.
        The data that is being encapsulated:
        - 'a' is the first operand.
        - 'b' is the second operand
        - 'operation' is the operation that need to be performed on the operands.
        '''
        self.a = a # operand1
        self.b = b # operand2
        self.operation = operation # operation that needs to be performed (add, subtract, etc...)

    def calculate(self) -> Decimal:
        '''
        This method returns the result of method call to the operation that need to perform by encapsulating the operation execution, providing a clean interface to the users by
        not showing the internal details of the logic.

        Returns
        -------
        The result of arithmetic operation performed.
        '''
        return self.operation(self.a, self.b)

    @staticmethod
    def createCalculation(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
            '''
            This is a static method to create a calculation instance. This method will provide a way to create instance for Calculation class by doing encapsulation to ensure user will 
            interact with the class through defined interfaces.

            Parameters
            ----------
            a: Decimal , b: Decimal -> Operands of the calculation.
            operation: Callable[[Decimal,Decimal], Decimal] -> operation that needs to be performed 

            Returns
            -------
            Calculation instance with the specified operands and operation.
            '''
        return Calculation(a, b, operation)
    
    def __stringify__(self):
        """
        Converts the instance to a string representation of the Calculation object which can be used for debugging by showing the operation and operands in a readable format.

        Returns
        -------
        A string representation in the format of Calculation(a, b, operation_name)
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
