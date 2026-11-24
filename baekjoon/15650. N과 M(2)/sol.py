import sys
sys.stdin = open('input.txt', 'r')

def go():  
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1, N+1):
        if lst and lst[-1] > i:
            continue

        if visited[i]:
            continue
        
        visited[i] = True
        lst.append(i)
        go()
        lst.pop()
        visited[i] = False
    


T = 2
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [False] * (N+1)
    lst = []
    go()