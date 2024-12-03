class calculator:
    """A simple calculator class with static methods for vector operations."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Compute the dot product between two vectors"""
        result = [float(a) * float(b) for a, b in zip(V1, V2)]
        print(f"Dot product result: {sum(result)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Compute the addition between two vectors"""
        result = [float(a) + float(b) for a, b in zip(V1, V2)]
        print(f"Addition result: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Compute the subtraction between two vectors"""
        result = [float(a) - float(b) for a, b in zip(V1, V2)]
        print(f"Addition result: {result}")
