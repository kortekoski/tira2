from collections import deque

def solve(n,k):
    pakka = deque()

    for x in range(1, n+1):
        pakka.append(x)
    
    while k > 0:
        luku1 = pakka.popleft()
        luku2 = pakka.popleft()
        pakka.append(luku2)
        pakka.append(luku1)
        
        k -= 1

    return pakka.popleft()

if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875