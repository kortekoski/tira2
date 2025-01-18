result = {}

def count_sequences(n):
    if n == 0:
        return 1
    #if n in result:
    #    return result[n]
    result[0] = 1

    for i in range(2, n + 1, 2):
        result[i] = 0
        for j in range(i-2, -1, -2):
            result[i] += result[j] * result[i - j - 2]

    return result[n]

def count_sequences2(n):
    result = {}
    result[(0, 0)] = 1
    for i in range(1, n + 1):
        result[(0, i)] = 0
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            result[(i, j)] = 0
            if j + 1 <= n:
                result[(i, j)] += result[(i - 1, j + 1)]
            if j - 1 >= 0:
                result[(i, j)] += result[(i - 1, j - 1)]
    return result[(n, 0)]

if __name__ == "__main__":
    print(count_sequences(100)) # 1978261657756160653623774456
    print(count_sequences2(100)) # 1978261657756160653623774456