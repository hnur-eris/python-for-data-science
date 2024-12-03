import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a unique 15-character alphanumeric string
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class to represent a student with optional attributes for
    name, surname, id, and other metadata.
    """
    name: str
    surname: str
    activate: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        Additional initialization after the dataclass-generated __init__ method
        """
        self.login = self.name[0].capitalize() + self.surname
