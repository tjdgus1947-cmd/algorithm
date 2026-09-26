import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    rotate_num = N // 4
    arr = input().strip()
    S = set()
    lst = []
    result_lst = []
    for _ in range(rotate_num):
        for i in range(0, N, rotate_num):
            S.add(arr[i:i+rotate_num])
        arr = arr[-1] + arr[:-1]
    for s in S:
        lst.append(s)
    for l in lst:
        num = int(l, 16)
        result_lst.append(num)
    result_lst.sort(reverse=True)
    result = result_lst[K-1]
    print(f"#{tc} {result}")