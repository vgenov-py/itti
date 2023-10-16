class Std:
    def __init__(self,x:list) -> None:
        self.x = x
    
    @property
    def n(self) -> int:
        return len(self.x)
    
    @property
    def mean(self) -> float:
        return sum(self.x)/self.n
    
    @property
    def variance(self) -> float:
        result = 0
        for v in self.x:
            result += (v - self.mean )**2
        return sum(result)/self.n
        return sum((v - self.mean)**2 for v in self.x)/self.n

    @property
    def cuasi_variance(self) -> float:
        return sum((v - self.mean)**2 for v in self.x)/(self.n-1)
    
    @property
    def standard_deviation(self) -> float:
        return self.variance**0.5


if __name__ == "__main__":
    Test_1 = Std([90,300,100,200])
    # standard deviation
    print(Test_1.variance)