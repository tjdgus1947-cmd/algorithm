import sys
sys.stdin = open('input.txt', 'r')
from itertools import product

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []
    answer = float('inf')

    for y in range(N):
        for x in range(N):
            if arr[y][x] ==1:
                people.append((y,x))
            if 2<= arr[y][x] <=10 :
                stairs.append((y,x,arr[y][x]))

    for order in product(range(2), repeat=len(people)):
        arrive = [[],[]]
        for i in range(len(people)):
            py, px = people[i][0], people[i][1]
            sy, sx = stairs[order[i]][0], stairs[order[i]][1]
            dist = abs(py-sy) + abs(px-sx)
            arrive[order[i]].append(dist)

        result = 0
        for s in range(2):
            times = sorted(arrive[s])
            K = stairs[s][2]
            end = []
            for i in range(len(times)):
                start = times[i] + 1
                if i >= 3:
                    start = max(start, end[i-3])
                end.append(start + K)
            if end:
                result = max(result, end[-1])
        answer = min(answer, result)

    print(f"#{tc} {answer}")