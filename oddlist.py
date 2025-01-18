from itertools import permutations

def count(n, x):
    if n == 1:
        return 1

    numerot = [x for x in range(1, n+1)]

    permutaatiot = permutations(numerot)

    xpermut = filter(lambda y: (y[0] == x), permutaatiot)

    counter = 0
    listat = {}

    for nrot in xpermut:
        listat[nrot] = []
        ok = True

        for i in range(1, n):
            if (nrot[i-1] + nrot[i]) in listat[nrot]:
                ok = False
            
            listat[nrot].append(nrot[i-1] + nrot[i])
        
        if ok:
            print(nrot)
            counter += 1
    
    return counter


if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(2, 1)) # 1
    #print(count(8, 5)) # 830