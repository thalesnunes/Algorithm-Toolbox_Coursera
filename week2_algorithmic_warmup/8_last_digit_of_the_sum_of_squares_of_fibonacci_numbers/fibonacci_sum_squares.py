# Uses python3
from sys import stdin

def get_fibonacci_last_digit(n):
    if n < 1:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(n - 1):
        prev, curr = curr % 10, (prev + curr) % 10

    return curr % 10

def fibonacci_sum_squares_naive(n):
    
    vert = get_fibonacci_last_digit(n % 60)
    horiz = get_fibonacci_last_digit((n + 1) % 60)
    return (vert * horiz) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
