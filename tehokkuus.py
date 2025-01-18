import math
import time
import random
from decimal import *
from collections import deque
import heapq

result = {}

def count_sequences1(n):
    if n == 0:
        return 1
    if n in result:
        return result[n]
    count = 0
    for i in range(2, n + 1, 2):
        count += count_sequences1(i - 2) * count_sequences1(n - i)
    result[n] = count
    return count

def count_sequences2(n):
    nimittaja = n // 2 + 1

    ncr = math.comb(n, n // 2)

    getcontext().prec = 100

    nimittaja2 = Decimal(1) / Decimal(nimittaja)

    result = nimittaja2 * ncr

    return int(result)

def deque_test(n):
    pakka = deque()

    aloitusaika = time.time()
    for x in range(1, n+1):
        pakka.append(x)
    suoritusaika = time.time() - aloitusaika
    print("aika lisäykseen:", suoritusaika)

    aloitusaika2 = time.time()
    while n > 0:
        pakka.popleft()
        n -= 1
    suoritusaika2 = time.time() - aloitusaika2
    print("aika poistoon:", suoritusaika2)

def random_heap(t):
    lista = []

    for i in range(0, len(t)):
        heapq.heappush(lista, t[i])

    counted = n // 10
    summa = 0

    while counted > 0:
        summa += heapq.heappop(lista)
        counted -= 1
    
    return summa

def random_list(t):
    jlista = sorted(t)
    counted = n // 10
    summa = 0

    for i in range(0, counted):
        summa += jlista[i]
    
    return summa


if __name__=="__main__":
    lista = []

    n = 10**6

    while n > 0:
        randomluku = random.randint(1, 10**9)
        lista.append(randomluku)
        n -= 1

    lista2 = lista.copy()

    aloitusaika1 = time.time()
    random_list(lista)
    suoritusaika1 = time.time() - aloitusaika1
    print("aika:", suoritusaika1)

    aloitusaika2 = time.time()
    random_heap(lista2)
    suoritusaika2 = time.time() - aloitusaika2
    print("aika:", suoritusaika2)
    
    #for i in range(1, 8):
    #    aloitusaika = time.time()
    #    n = i * 1000
    #    tulos = count_sequences2(n)
    #    suoritusaika = time.time() - aloitusaika
    #    print("n =", n, "aika:", suoritusaika)

    