# Uses python3
import sys

def optimal_weight(W, w):
    
    result = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for wei in range(1, W+1):
            result[i][wei] = result[i-1][wei]
            if w[i-1] <= wei:
                val = result[i-1][wei - w[i-1]] + w[i-1]
                if val > result[i][wei]:
                    result[i][wei] = val

    return result[n][W]

if __name__ == '__main__':
    W, n = [*map(int, input().split())]
    w = [*map(int, input().split())]
    print(optimal_weight(W, w))
