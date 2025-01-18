import heapq

class Median:
    def __init__(self):
        self.numbers = []
        self.index = 0
        self.medi = 0

    def add(self, x):
        heapq.heappush(self.numbers, x)

        if len(self.numbers) == 1:
            pass
        elif len(self.numbers) % 2 == 0:
            self.index = len(self.numbers) // 2 - 1
        elif len(self.numbers) > 1 and len(self.numbers) % 2 != 0:
            self.index = len(self.numbers) // 2


    def median(self):
        returned = []

        counter = self.index

        while counter >= 0:
            pienin = heapq.heappop(self.numbers)
            returned.append(pienin)
            counter -= 1

        if len(returned) == 0:
            return self.numbers[0]
        
        luku = returned[-1]
        
        while len(returned) > 0:
            heapq.heappush(self.numbers, returned.pop())

        return luku

if __name__ == "__main__":
    m = Median()
    m.add(10)
    print(m.median())
    m.add(9)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(10)
    print(m.median())
    m.add(10)
    print(m.median())
    m.add(3)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(7)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(5)
    print(m.median())