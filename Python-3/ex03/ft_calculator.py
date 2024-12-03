class calculator:
    """ Basic calculator Class"""
    def __init__(self, numbers):
        """ Initialize the calculator with a list of numbers """
        self.numbers = numbers

    def __add__(self, object) -> None:
        """ Add an object to the calculator"""
        if not isinstance(object, (int, float)):
            print("Addition only supports object values (int or float)")
            return None
        result = [a + object for a in self.numbers]
        print(f"Addition result: {result}")
        self.numbers = (result)
        return self.numbers

    def __mul__(self, object) -> None:
        """ Multiply an object to the calculator"""
        if not isinstance(object, (int, float)):
            print("Addition only supports object values (int or float)")
            return None
        result = [a * object for a in self.numbers]
        print(f"Addition result: {result}")
        self.numbers = (result)
        return self.numbers

    def __sub__(self, object) -> None:
        """ Subtract an object from the calculator"""
        if not isinstance(object, (int, float)):
            print("Addition only supports object values (int or float)")
            return None
        result = [a - object for a in self.numbers]
        print(f"Addition result: {result}")
        self.numbers = (result)
        return self.numbers

    def __truediv__(self, object) -> None:
        """ Divide the calculator by an object"""
        if not isinstance(object, (int, float)):
            print("Addition only supports object values (int or float)")
            return None
        result = []
        for a in self.numbers:
            if a != 0:
                result.append(a / object)
            else:
                raise ValueError("The number cannot divide by zero")

        print(f"Addition result: {result}")
        self.numbers = (result)
        return self.numbers
