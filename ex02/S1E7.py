from S1E9 import Character


class Baratheon(Character):
    """A member of the House of the deer"""

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Declare a member of the House Baratheon"""
        return (f"{self.family_name}, {self.eyes}, {self.hairs}")

    def __repr__(self):
        """Declare a member of the House Baratheon"""
        return
        (f"Vector : ('{self.family_name}','{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """A House whos members really love each others"""
    def __init__(self, first_name, is_alive=True, eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Declare a member of the House Lannister"""
        return (f"Vector : ({self.family_name}, {self.eyes}, {self.hairs})")

    def __repr__(self):
        """Declare a member of the House Lannister"""
        return
        (f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister"""
        return cls(first_name, is_alive)
