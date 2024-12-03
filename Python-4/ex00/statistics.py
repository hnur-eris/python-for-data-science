
class Arithmetic():
    """class for arithmetic operations"""
    def __init__(self, number: list):
        """
        Initializes the arithmetic class with a list of numbers.
        """
        self.number = sorted(list(number))
        self.len = len(number)

    def mean(self):
        """"mean the list of numbers"""
        return sum(self.number) / self.len

    def median(self):
        """"median the list of numbers"""
        if self.len % 2 == 0:
            m_id1 = self.number[self.len // 2]
            mid2 = self.number[self.len // 2 - 1]
            res = (m_id1 + mid2) / 2
        else:
            res = self.number[self.len // 2]
        print(f"median : {res}")

    def quartile(self):
        """"quantile the list of numbers"""
        f_quarter = self.len // 4
        s_quarter = f_quarter + self.len // 2
        print(
            "quartile :",
            f"[{float(self.number[f_quarter])}",
            f"{float(self.number[s_quarter])}]"
        )

    def var(self):
        """"variance the list of numbers"""
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.number) / self.len
        return variance

    def std(self):
        """standart derivation the numbers"""
        std_dev = self.var() ** 0.5
        print(f"std : {std_dev}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    A function to calculate statistics from a list of numbers.
    """
    calc = Arithmetic(args)
    for value in kwargs.values():
        if not args:
            print("ERROR")
            continue
        if value == "mean":
            print(f"mean : {calc.mean()}")
        elif value == "median":
            calc.median()
        elif value == "quartile":
            calc.quartile()
        elif value == "std":
            calc.std()
        elif value == "var":
            print(f"var : {calc.var()}")
        else:
            continue
