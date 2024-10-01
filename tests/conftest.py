import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_of_records):
    mappings = {
        'add' : add,
        'subtract' : subtract,
        'multiply' : multiply,
        'divide' : divide
    }

    for i in range(num_of_records) : 
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if i % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation = fake.random_element(elements = list(mappings.keys()))
        operation_method = mappings[operation]

        if operation_method == divide:
            b = Decimal('1') if b == Decimal('0') else b
        
        try:
            if operation_method == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_method(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation, operation_method, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_of_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_of_records))
        _parameters = [(a, b, opr_name if 'operation' in metafunc.fixturenames else op_func, expected)  for a, b, opr_name, op_func, expected in parameters]
        metafunc.parametrize("a, b, operation, expected", _parameters)