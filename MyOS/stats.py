class Stats:
    def __init__(self, x:list,y:list) -> None:
        self.x = x
        self.y = y

    def mean(self):
        return sum(self.x)/len(self.x)
    
method1 = Stats(y=[1,2,3,4], x=[1,2,3,4])
method2 = Stats([1,5,3,4], [1,9,3,4])

method1.mean()
method2.mean()
x = [1,2,2,3]

def mean(x:list) -> float:
    return sum(x)/len(x)

method1_mean = mean(x)
method2_mean = mean(x)