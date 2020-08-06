# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m1] = a[m1], a[i]
        elif a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2


def randomized_quick_sort_3(a, l, r):
    if l >= r:
        return None
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort_3(a, l, m1 - 1)
    randomized_quick_sort_3(a, m2 + 1, r)
    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort_2(a, l, r):
    if l >= r:
        return None
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort_2(a, l, m - 1)
    randomized_quick_sort_2(a, m + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = [*map(int, input().split())]
    randomized_quick_sort_3(a, 0, n - 1)
    print(*a)
    # while True:
    #     n = random.randint(1, 100000)
    #     a = []
    #     for _ in range(n):
    #         a.append(random.randint(1, 1000000000))
    #     case3 = randomized_quick_sort_3(a, 0, n-1)
    #     case2 = randomized_quick_sort_2(a, 0, n-1)
    #     if case3 != case2:
    #         print(f'Erro: a = {a}, 2 = {case2}, 3 = {case3}')
    #         break
    #     else:
    #         print('OK')
