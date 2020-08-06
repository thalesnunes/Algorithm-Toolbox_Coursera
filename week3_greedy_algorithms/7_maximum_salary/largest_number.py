#Uses python3


def largest_number(vec):
    
    max_len = len(str(max(vec)))
    return ''.join(sorted((str(v) for v in vec), reverse=True, key=lambda num: num*(max_len * 2 // len(num))))

if __name__ == '__main__':
    doe = int(input())
    vec = [*map(int, input().split())]
    print(largest_number(vec))
    
