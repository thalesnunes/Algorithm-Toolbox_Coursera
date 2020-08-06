# Uses python3
import sys

def get_majority_element(a, left, right):

    map_num = set(a)
    count_dict = {key: 0 for key in map_num}
    for elem in a:
        count_dict[elem] += 1
    if max(count_dict.values()) > right/2:
        return 0
    else:
        return -1

if __name__ == '__main__':
    n = int(input())
    a = [*map(int, input().split())]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
