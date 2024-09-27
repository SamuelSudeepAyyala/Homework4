from calculator.Calculation import Calculation
from decimal import Decimal
from typing import Callable,List

class Calculationhistory:
    history = []

    @classmethod
    def add_history(cls,Calculation: Calculation):
        cls.history.append(Calculation)
    
    @classmethod
    def delete_history(cls):
        cls.history.clear()
        
    @classmethod
    def print_history(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def get_latest_history(cls):
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def get_with_operation(cls, operation:str) -> List[Calculation]:
        return [i for i in cls.history if i.operation.__name__ == operation]
