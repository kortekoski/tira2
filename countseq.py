def count(t):
    result = {}

    result[0] = 1

    for i in range(1, len(t)):
        result[i] = 1
        for j in range(0, i):
            if t[j] < t[i]:
                result[i] += result[j]
    
    summa = 0
    
    for x in result.values():
        summa += x

    return summa

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37