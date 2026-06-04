class calculator:
    """Calculate"""
    def __init__(self, object):
        """init"""
        self.object = object

    def __add__(self, object) -> None:
        """add"""
        self.object = [elem + object for elem in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """multiply"""
        self.object = [elem * object for elem in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """substract"""
        self.object = [elem - object for elem in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """divide"""
        try:
            self.object = [elem / object for elem in self.object]
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        print(self.object)


def main():
    """entry point of the programm"""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 / 0


if __name__ == "__main__":
    main()
