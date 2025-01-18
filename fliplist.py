from collections import deque

class FlipList:
    def __init__(self):
        self.fliplist = deque()
        self.flippedlist = deque()
        self.flipped = False

    def push_first(self,x):
        if not self.flipped:
            self.fliplist.appendleft(x)
            self.flippedlist.append(x)
        else:
            self.fliplist.append(x)
            self.flippedlist.appendleft(x)

    def push_last(self,x):
        if not self.flipped:
            self.fliplist.append(x)
            self.flippedlist.appendleft(x)
        else:
            self.fliplist.appendleft(x)
            self.flippedlist.append(x)

    def pop_first(self):
        if not self.flipped:
            self.flippedlist.pop()
            return self.fliplist.popleft()
        else:
            self.fliplist.pop()
            return self.flippedlist.popleft()   
        

    def pop_last(self):
        if not self.flipped:
            self.flippedlist.popleft()
            return self.fliplist.pop()
        else:
            self.fliplist.popleft()
            return self.flippedlist.pop()

    def flip(self):
        if self.flipped:
            self.flipped = False
        else:
            self.flipped = True

if __name__ == "__main__":
    f = FlipList()
    f.push_last(2)
    f.push_last(3)
    f.push_last(1)
    f.flip()
    print(f.pop_last())
    f.flip()
    print(f.pop_last())
    f.flip()
    print(f.pop_last())