import sys
sys.stdin = open('input.txt', 'r')


def go():
    if len(lst) == M:
        result.append(' '.join(map(str, lst)))
        return

    for i in range(1, N+1):
        lst.append(i)
        go()
        lst.pop()

T = 3
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    result = []

    go()

    print('\n'.join(result))