


class calculator():

    numbers = []

    def __init__(self, object):
        self.numbers = object
    
    def __add__(self, object) -> None:
        for i, val in enumerate(self.numbers):
            self.numbers[i] = val + object
        print(self.numbers)
        
    
    def __mul__(self, object) -> None:
        for i, val in enumerate(self.numbers):
            self.numbers[i] = val * object
        print(self.numbers)
    
    def __sub__(self, object) -> None:
        for i, val in enumerate(self.numbers):
            self.numbers[i] = val - object
        print(self.numbers)

    def __truediv__(self, object) -> None:
        if object != 0:
            for i, val in enumerate(self.numbers):
                self.numbers[i] = val / object
            print(self.numbers)

