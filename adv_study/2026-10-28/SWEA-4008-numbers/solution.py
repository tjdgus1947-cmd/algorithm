T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cals = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mx = float("-inf")
    mn = float("inf")

    stack = [(1, nums[0], cals[0], cals[1], cals[2], cals[3])]
    while stack:
        idx, cur, p, m, t, d, = stack.pop()
        if idx == N:
            mx = max(mx, cur)
            mn = min(mn, cur)
            continue
        num = nums[idx]
        if p > 0 : stack.append((idx+1, cur+num, p-1, m, t, d))
        if m > 0 : stack.append((idx+1, cur-num, p, m-1, t, d))
        if t > 0 : stack.append((idx+1, cur*num, p, m, t-1, d))
        if d > 0 : stack.append((idx+1, int(cur/num), p, m, t, d-1))
    result = mx - mn

    print(f"#{tc} {result}")