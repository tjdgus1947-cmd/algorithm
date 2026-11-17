import sys
sys.stdin = open('input.txt', 'r')

def go(node):
    visited[node] = True
    for n in adj_lst[node]:
        if visited[n] == False:
            go(n)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_lst = [[] for _ in range(N+1)]
    for _ in range(M):
        n, m = map(int, input().split())
        adj_lst[n].append(m)
        adj_lst[m].append(n)
    visited = [False] * (N+1)
    result = 0
    for i in range(1, N+1):
        if visited[i] == False:
            go(i)
            result += 1

    print(f"#{tc} {result}")