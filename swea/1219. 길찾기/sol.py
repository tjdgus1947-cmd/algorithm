import sys
sys.stdin = open('input.txt', 'r')

T = 10

def go(node):
    visited[node] = True
    for nxt_node in adj_lst[node]:
        if visited[nxt_node] == False:
            go(nxt_node)

for tc in range(1, T+1):
    t,  N = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_lst = [[] for _ in range(100)]
    visited = [False] * 100
    for k in range(0, len(arr), 2):
        adj_lst[arr[k]].append(arr[k+1])

    go(0)
    result = 1 if visited[99] == True else 0
    print(f"#{tc} {result}")
    