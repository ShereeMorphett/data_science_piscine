from S1E7 import Baratheon
# In this exercise, you will create a monster: Joffrey Baratheon.
# This is so risky!
# There is something inconsistent with this new "false" king.
# You must use the Properties to change the physical characteristics of our new king.
# The prototype of Class is



class King(Baratheon):
    def __init__(self,  char_name: str, is_alive=True):
        """Uses the base classes constructor
        Args:
            char_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """        
        super().__init__(char_name, is_alive)

    
    def set_eyes(self, color:str):
        self.eye_color = color
        
    def set_hairs(self, color:str):
        self.hair_color = color
    
    def get_eyes(self):
        return self.eye_color
    
    def get_hairs(self):
        return self.hair_color
    
