import heapq

def smallest(n):
    alkiot = [1]

    steps = n

    while steps > 0:
        x = heapq.heappop(alkiot)
        heapq.heappush(alkiot, 2 * x)
        heapq.heappush(alkiot, 3 * x)
        steps -= 1
    
    return heapq.heappop(alkiot)

if __name__ == "__main__":
   # print(smallest(1)) # 2
    #print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552