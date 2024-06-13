from S1E9 import Character


# Create two families that inherit from the Character class, that we can instantiate
# without going through the Character class. Find a solution so that "__str__" and
# "__repr__" return strings and not objects. Write a Class method to create characters
# in a chain.


class Baratheon(Character):
    def __init__(self,  char_name: str, is_alive=True):
        """Uses the base classes constructor
        Args:
            char_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """        
        super().__init__(char_name, is_alive)
        self.family_name = "Baratheon"
        self.eye_color = "brown"
        self.hair_color = "dark"
    
    
    def __str__(self):
        """_s
        Returns:
            _type_: _description_
        """        
        return f"Vector: ('{self.family_name}', '{self.eye_color}', '{self.hair_color}')"

    def __repr__(self):
        return self.__str__()
    
    def die(self):
        """sets is_alive to False using base class die implementation"""
        super().die()


class Lannister(Character):
    def __init__(self,  char_name: str, is_alive=True):
        """Uses the base classes constructor
        Args:
            char_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """        
        super().__init__(char_name, is_alive)
        self.family_name = "Lannister"
        self.eye_color = "blue"
        self.hair_color = "light"


    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eye_color}', '{self.hair_color}')"

    def __repr__(self):
        return self.__str__()


    def die(self):
        """sets is_alive to False using base class die implementation"""
        super().die()


    def create_lannister(name: str, dead: bool):
        return Lannister(name, dead)