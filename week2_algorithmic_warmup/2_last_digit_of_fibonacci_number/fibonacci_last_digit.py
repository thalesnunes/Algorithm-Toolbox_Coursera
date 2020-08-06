# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    seq = [0, 1]

    while len(seq) <= n:
        seq.append(seq[-2]%10+seq[-1]%10)

    return seq[-1] % 10

if __name__ == '__main__':
    n1 = int(input())
    print(get_fibonacci_last_digit_naive(n1))
