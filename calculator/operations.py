from decimal import Decimal

# Defines a function to add two numbers
def add(a: Decimal, b: Decimal) -> Decimal:
    '''
    Adds two numbers and results the result
    Args: 
    a (Decimal): the first number
    b (Decimal): the second number

    It returns Decimal: The sum of a and b
    '''
    return a + b

# Defines a function to subtract two numbers
def subtract(a: Decimal, b: Decimal) -> Decimal:
    '''
    Subtracts two numbers and results the result
    Args: 
    a (Decimal): the first number
    b (Decimal): the second number

    It returns Decimal: The subtraction of b from a
    '''
    return a - b

# Defines a function to multiply two numbers
def multiply(a: Decimal, b: Decimal) -> Decimal:
    '''
    Multiplies two numbers and results the result
    Args: 
    a (Decimal): the first number
    b (Decimal): the second number

    It returns Decimal: The product of a and b
    '''
    return a * b

# Defines a function to divide two numbers
def divide(a: Decimal, b: Decimal) -> Decimal:
    '''
    Adds two numbers and results the result
    Args: 
    a (Decimal): the first number
    b (Decimal): the second number

    It raises ValueError if b is equal to 0. 
    else it will return the result of dividing a by b
    '''
    if b == 0 :
        raise ValueError("Division By Zero is not allowed!")
    else:
        return a / b