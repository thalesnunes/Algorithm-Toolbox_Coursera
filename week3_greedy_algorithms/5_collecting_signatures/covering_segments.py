# Uses python3
import sys

def optimal_points(segments):

    points = []
    while segments:
        end1 = segments[0][1]
        points.append(end1)
        to_remove = []
        for line in segments:
            if line[0] <= end1 <= line[1]:
                to_remove.append(line)
        segments = [value for value in segments if value not in to_remove]          
        
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append([int(x) for x in input().split()])
    segments.sort(key=lambda elem: elem[1])
    points = optimal_points(segments)
    print(len(points))
    print(*points)
