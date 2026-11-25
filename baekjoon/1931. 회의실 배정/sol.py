import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end = 0

for s, e in times:
    if s >= end:
        cnt += 1
        end = e

print(cnt)


# def max_meetings(times):
#     times.sort(key= lambda x:(x[1], x[0]))
#     cnt, end = 0, 0
#     for s, e in times:
#         if s >= end:
#             cnt +=1
#             end = e
#     return cnt

# N = int(input())
# times = [tuple(map(int, input().split())) for _ in range(N)]
# print(max_meetings(times))