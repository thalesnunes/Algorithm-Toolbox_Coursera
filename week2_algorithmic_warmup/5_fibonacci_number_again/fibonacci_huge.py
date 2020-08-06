# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    rep = [0, 1]
    prev = 0
    curr = 1
    for i in range(n - 1):
        temp = prev
        prev = curr % m
        curr = (temp + curr) % m
        rep.append(curr)
        if curr == 1 and prev == 0:
            index = (n % (i + 1))
            return rep[index]
    return curr



if __name__ == '__main__':
    input1 = str(input())
    n, m = map(int, input1.split())
    print(get_fibonacci_huge_naive(n, m))
