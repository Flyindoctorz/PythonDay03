from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A monster of consanguinity"""

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def set_eyes(self, eyes):
        self.eyes= eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return (self.eyes)

    def get_hairs(self):
        return (self.hairs)



def main():
    """entry point of the programm"""
    print(King.__mro__)


if __name__ == "__main__":
    main()