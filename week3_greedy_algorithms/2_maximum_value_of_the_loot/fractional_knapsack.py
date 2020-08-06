# Uses python3
import sys

def get_optimal_value(W, stin, wei):
    
    value = 0
    for _ in range(len(wei)):
        if W == 0:
            return value
        now = max([v for v in stin if wei[stin.index(v)] > 0])
        ind = stin.index(now)
        a = min(wei[ind], W)
        value += a*(stin[ind])
        wei[ind], W = wei[ind] - a, W - a

    return value


if __name__ == "__main__":
    
    inp = str(input())
    n, W = map(int, inp.split())
    stin = []
    wei = []
    for _ in range(n):
        s = [int(x) for x in str(input()).split()]
        wei.append(s[1])
        stin.append(s[0]/s[1])
    opt_value = get_optimal_value(W, stin, wei)
    print("{:.10f}".format(opt_value))
