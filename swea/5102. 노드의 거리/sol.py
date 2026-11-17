import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def go(node, length):
    q = deque([(node, length)])
    visited[node] = True
    while q:
        node, length = q.popleft()
        for n in adj_lst[node]:
            if n == G:
                return length+1
            if visited[n] == False:
                visited[n] = True
                q.append((n, length+1))
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]
    for _ in range(E):
        n, m = map(int, input().split())
        adj_lst[n].append(m)
        adj_lst[m].append(n)
    S, G = map(int, input().split())
    visited = [False] * (V+1)
    result = go(S, 0)

    print(f"#{tc} {result}")



    