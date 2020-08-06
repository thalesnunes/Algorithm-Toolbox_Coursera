#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(input())
    a = [*map(int, str(input()).split())]
    a.sort()
    b = [*map(int, str(input()).split())]
    b.sort()
    print(max_dot_product(a, b))
    
