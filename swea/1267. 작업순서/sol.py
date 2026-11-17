import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

for tc in range(1,11):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))

    adj = [[] for _ in range(V+1)]
    front = [0] * (V+1)

    for i in range(0, len(lst), 2):
        a, b = lst[i], lst[i+1]
        adj[a].append(b)
        front[b] += 1

    q = deque()

    for i in range(1, V+1):
        if front[i] == 0:
            q.append(i)

    result = []
    while q:
        cur = q.popleft()
        result.append(cur)
        for nxt in adj[cur]:
            front[nxt] -= 1
            if front[nxt] == 0:
                q.append(nxt)

    print(f"#{tc}", *result)