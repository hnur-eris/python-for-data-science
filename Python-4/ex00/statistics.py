
class Arithmetic():
    def __init__(self, number:list[float]):
        self.number = sorted(list(number))
        self.len = len(number)
    def mean(self):
        return sum(self.number) / self.len

    def median(self):
        if self.len % 2 == 0:
            m_id1 = self.number[self.len // 2]
            mid2 = self.number[self.len // 2 - 1]
            res = (m_id1 + mid2) / 2
        else:
            res = self.number[self.len // 2]
        print(f"median : {res}")
    
    def quartile(self):
        f_quarter = self.len // 4
        s_quarter = f_quarter + self.len // 2
        print(f"quartile : [{float(self.number[f_quarter])}, {float(self.number[s_quarter])}]")        

    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.number) / self.len
        return variance
    def std(self):
        std_dev = self.var() ** 0.5
        print(f"std : {std_dev}")

def ft_statistics(*args: any, **kwargs: any) -> None:

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
