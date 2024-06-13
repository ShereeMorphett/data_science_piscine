from abc import ABC, abstractmethod

# Create an abstract class "character" which can take a first_name as first parameter,
# is_alive as second non mandatory parameter set to True by default and can change the
# health state of the character with a method that passes is_alive from True to False.
# And a "stark" class which inherits from Character



class Character(ABC):
    """Abstract base class for characters: contains name and is_alive
    """    
    def __init__(self, name: str, alive=True):
        """
        constructs the base class
        Args:
            name (str): _description_
            alive (bool, optional): _description_. Defaults to True.
        """        
        self.first_name = name
        self.is_alive = alive

    @abstractmethod
    def die(self):
        """sets is_alive to False""" 
        self.is_alive = False


class Stark(Character):
    """
    Args:
        Character (_type_): Character name and construction is_alive
    """    
    def __init__(self,  first_name: str, is_alive=True):
        """Uses the base classes constructor
        Args:
            char_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """        
        super().__init__(first_name, is_alive)

    def die(self):
        """sets is_alive to False using base class die implementation"""
        super().die()