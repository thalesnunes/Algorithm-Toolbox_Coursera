# python3
import sys


def compute_min_refills(d, m, stops):
    
    curr = 0
    refs = 0
    while curr <= len(stops)-2:
        last = curr
        while curr <= len(stops)-2 and stops[curr+1] - stops[last] <= m:
            curr += 1
        if curr == last:
            return -1
        if curr <= len(stops)-2:
            refs += 1
    return refs
        
    
if __name__ == '__main__':
    di = int(input())
    mi = int(input())
    deos = int(input())
    gas = str(input()).split()
    gas = [int(x) for x in gas]
    gas.insert(0, 0)
    gas.append(di)
    print(compute_min_refills(di, mi, gas))
