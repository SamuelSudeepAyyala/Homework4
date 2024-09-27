from calculator.Calculation import Calculation
from decimal import Decimal
from typing import Callable,List

class calculations:
    '''
    This class is used to manage the history of arithmetic calculations.

    Attributes
    ----------
    history -> This is initialised empty list to store all the instances of calculations performed. A list that stores instances of Calculation, representing the history of
    operations performed.

    '''
    history = [] # This list will hold the history of calculations.

    @classmethod
    def add_history(cls,Calculation: Calculation):
        """
        Adds a instance of calculation to the history.

        Parameters
        ----------
        Calculation : Calculation -> An instance of calculation class to be added to the history.
        """
        cls.history.append(Calculation)
    
    @classmethod
    def delete_history(cls):
        """
        This classmethod will clear the data inside the history list.
        """
        cls.history.clear()
        
    @classmethod
    def print_history(cls) -> List[Calculation]:
        """
        Return the list of Calculations in the history.

        Returns 
        -------
        List[Calculation] -> A list of calculation instances representing the history.
        """
        return cls.history
    
    @classmethod
    def get_latest_history(cls):
        """
        This method retrives the most recent Calculation from the history.

        Returns
        -------
        Calculation or None
        depending the history existance the function will return the most recent calculation or it will return None.
        """
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def get_with_operation(cls, operation:str) -> List[Calculation]:
        """
        This method will retrive the calculations that matches with the given operation.

        Parameters
        ----------
        operation : str -> This is the name of operation with which we need to filter the history.

        Returns
        -------
        List[Calculation] -> Returns the list of calculation instances that are matched with specific operation.
        """
        return [i for i in cls.history if i.operation.__name__ == operation]
