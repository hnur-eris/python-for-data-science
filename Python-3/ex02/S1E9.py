from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract base class representing a character
    with a first_name and a state of being alive.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the Character instance with a first_name
        and an optional alive status.

        Attributes:
        first_name (str): The first_name of the character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.

        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to handle the character's death.
        Must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    A subclass of Character representing a member of the Stark family.

    Methods:
        die(): Handles the death of the character.
    """
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
            print(f"{self.first_name} has died.")
            self.is_alive = False
