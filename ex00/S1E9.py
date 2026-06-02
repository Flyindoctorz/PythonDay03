

class Character:
    """a character is alive"""
    def __init__(self, first_name, is_alive=True):
        """Initialize a character"""
        pass
    def die(self):
        """Drop.DEAD"""
        self.is_alive = False
        return

class Stark(Character):
    """The famous decimated House in GOT"""
    def __init__(self, first_name, is_alive=True):
        """Initialize a member of the House Stark"""
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
    def die(self):
        """Drop. DEAD"""
        self.is_alive = False
        return