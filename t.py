h, w = map(int, input().split())
arr =  [[0 for j in range(w)] for i in range(h)]
num = int(input())

for i in range(num):
    l, d, x, y = map(int, input().split())
    if d == 0: # 막대가 가로방향인 경우
        for j in range(l):
            arr[(x - 1)][(y - 1) + j] = 1
    else: # 막대가 세로방향인 경우
        for k in range(l):
            arr[(x - 1) + k][(y - 1)] = 1

for i in range(h):
    print(*arr[i])