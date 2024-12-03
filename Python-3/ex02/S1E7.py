from S1E9 import Character
# import pdb
# pdb.set_trace()


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new Baratheon character with default attributes.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The character's living status.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """
        Returns a human-readable string representation of Baratheon character

        Returns:
            str: A string describing the character's family,
            eye color, and hair color.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Returns developer friendly string representation of Baratheon character

        Returns:
            str: A string that provides unambiguous details about the character
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Handles the death of the Stark character.
        If the character is already dead, prints a message indicating that.
        Otherwise, sets the character's alive status to False and
        prints a death message.
        """
        if not self.is_alive:
            print(f"Baratheon's {self.first_name} is already dead.")
        else:
            self.is_alive = False


class Lannister(Character):
    """Representing the Lanniester family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new Lannister character with default attributes.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The character's living status.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Returns a human-readable string representation of Lannister character.

        Returns:
            str: A string describing the character's family,
            eye color, and hair color.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Returns a developer-friendly string representation of
        the Lannister character.

        Returns:
            str: A string that provides unambiguous details about the character
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Creates a new Lannister character using a class method.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The character's living status.
            Defaults to True.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)

    def die(self):
        """
        Handles the death of the Stark character.
        If the character is already dead, prints a message indicating that.
        Otherwise, sets the character's alive status to False and
        prints a death message.
        """
        if not self.is_alive:
            print(f"{self.first_name} is already dead.")
        else:
            # print(f"Lanniester's {self.first_name} has died.")
            self.is_alive = False

# genelde direk .__ diye erişilmezmiş bu yüzden bunları
# çağırmak için belli başlı fonksiyonlar üzerinden kullanılırmış

# dunder functions

# The __str__() method returns a human-readable, or informal,
# string representation of an object. This method is called by
# the built-in print(), str(), and format() functions.
# If you don’t define a __str__() method for a class,
# then the built-in object implementation calls the __repr__() method instead.


# The __repr__() method returns a more information-rich, or official,
# string representation of an object.
# This method is called by the built-in repr() function.
# If possible, the string returned should be a valid Python expression that
# can be used to recreate the object.
# In all cases, the string should be informative and unambiguous
