class calculator:
    """Calculate"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for elem1, elem2 in zip(V1, V2):
            res += elem1 * elem2
        print(res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for elem1, elem2 in zip(V1, V2):
            res.append(float(elem1 + elem2))
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for elem1, elem2 in zip(V1, V2):
            res.append(float(elem1 - elem2))
        print(res)


