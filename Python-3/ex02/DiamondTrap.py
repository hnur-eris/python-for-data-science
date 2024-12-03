from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """King constructor"""
        super().__init__(first_name, is_alive)
        self.kingdom = "Westeros"

    def set_eyes(self, eyes):
        """Set the character's eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the character's hair color"""
        self.hairs = hairs

    def get_eyes(self):
        """Get the character's eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get the character's hair color"""
        return self.hairs

    def die(self):
        """Handle the death of the King"""
        super().die()
