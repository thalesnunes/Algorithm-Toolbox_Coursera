# Uses python3
import sys

def gcd(a, b):

    alinha = a % b
    if alinha == 0:
        return b
    result = gcd(b, alinha)

    return result

if __name__ == "__main__":

    input1 = str(input())
    a, b = map(int, input1.split())
    print(gcd(a, b))
