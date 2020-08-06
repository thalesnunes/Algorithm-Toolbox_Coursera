# Uses python3
import sys

def lcm_naive(a, b):
    
    lcm = (a*b)//gcd(a, b)

    return lcm

def gcd(a, b):

    alinha = a % b
    if alinha == 0:
        return b
    result = gcd(b, alinha)

    return result

if __name__ == '__main__':
    input1 = str(input())
    a, b = map(int, input1.split())
    print(lcm_naive(a, b))

