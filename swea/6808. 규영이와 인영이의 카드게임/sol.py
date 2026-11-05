# 재귀 사용

import sys
sys.stdin = open('input.txt', 'r')

def go(i, gyu_score, young_score):
    global win, lose                          # ④
    if i == 9:
        if gyu_score > young_score:           # ① 비교는 끝 조건 안에서
            win += 1
        elif young_score > gyu_score:
            lose += 1
        return
    for j in range(9):                        # ② 라운드 i, 인영이 카드 j
        if visited[j]:
            continue
        visited[j] = True
        if gyu[i] > young[j]:                 # ③ += 안 쓰고 더한 값을 바로 넘김
            go(i+1, gyu_score + gyu[i] + young[j], young_score)
        else:
            go(i+1, gyu_score, young_score + gyu[i] + young[j])
        visited[j] = False

T = int(input())
for tc in range(1, T+1):
    gyu = list(map(int, input().split()))
    young = []
    for c in range(1, 19):
        if c not in gyu:
            young.append(c)
    win = 0
    lose = 0
    visited = [False] * 9
    go(0, 0, 0)                               # ⑤
    print(f"#{tc} {win} {lose}")