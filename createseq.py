def find(t):
    result = {}

    result[0] = 1

    for i in range(1, len(t)):
        result[i] = 1
        for j in range(0, i):
            if t[j] < t[i]:
                result[i] = max(result[i], result[j] + 1)

    suurin = max(list(result.values()))
    suurinavain = list(result.values()).index(suurin)
    print(result)

    solution = [t[list(result.values()).index(suurin)]]
    suurin -= 1

    while suurin > 0:
        for key, value in result.items():
            if value == suurin:
                if t[key] < solution[-1] and key < suurinavain:
                    solution.append(t[key])
                    suurinavain = key
                    suurin -= 1

    return sorted(solution)

if __name__ == "__main__":
    #print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    #print(find([1, 1, 1, 1])) # [1]
    #print(find([5, 4, 3, 2, 1])) # [3]
    #print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]
    #print(find([9, 6, 10, 10, 3, 6, 7, 6, 5, 7]))
    #print(find([3, 6, 10, 8])) # 3, 6, 8
    print(find([2, 4, 8, 9, 5, 1]))