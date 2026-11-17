import sys
sys.stdin = open('input.txt', 'r')

def go(node):
    visited[node] = True
    for n in adj_lst[node]:
        if visited[n] == False:
            go(n)


T = 10
for tc in range(1, T+1):
    t, n = map(int, input().split())
    lst = list(map(int, input().split()))
    adj_lst = [[] for _ in range(100)]
    for i in range(0,2*n,2):
        adj_lst[lst[i]].append(lst[i+1])
    visited = [False] * 100
    result = 0
    visited[0] = True
    go(0)
    if visited[99] == True:
        result = 1

    print(f"#{tc} {result}")