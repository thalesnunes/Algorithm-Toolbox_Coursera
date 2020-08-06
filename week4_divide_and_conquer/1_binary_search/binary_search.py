# Uses python3
import sys
import math

def binary_search(a, x, low, high):

    while low <= high:
        
        mid = low + (high-low)//2
        
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    a = [*map(int, input().split())]
    a = a[1:]
    numbs = [*map(int, input().split())]
    numbs = numbs[1:]
    for x in numbs:
        low = 0
        high = len(a) - 1
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, low, high), end = ' ')
