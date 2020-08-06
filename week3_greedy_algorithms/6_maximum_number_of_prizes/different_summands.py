# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n <= 2:
        return [n]
    cand = 1
    while n > 0:
        if n - cand >= 0:
            summands.append(cand)
            n -= cand
            cand += 1
        else:
            summands[-1] += n
            n -= cand

    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
