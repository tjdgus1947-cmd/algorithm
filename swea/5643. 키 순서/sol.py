import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def go(i, graph):
    q = deque([i])
    visited = [False] * (N+1)
    visited[i] = True
    cnt = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == False:
                cnt += 1
                visited[nxt] = True
                q.append(nxt)

    return cnt
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    longer = [[] for _ in range(N+1)]
    shorter = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        longer[a].append(b)
        shorter[b].append(a)

    result = 0
    for i in range(1, N+1):
        if go(i,shorter) + go(i,longer) == N-1:
            result += 1

    print(f"#{tc} {result}")