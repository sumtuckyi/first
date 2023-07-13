arr = [list(map(int, input().split())) for _ in range(19)] # 세로줄 갯수 만큼 반복해서 입력 받음
n = int(input())

for _ in range(n):
    x, y = map(lambda z: int(z) - 1, input().split())# 좌표값을 int로 변환함과 동시에 1씩 빼고 싶을 때 람다 함수 이용
    for j in range(19):
        if arr[int(x)][j] == 0:
            arr[int(x)][j] = 1
        else:
            arr[int(x)][j] = 0
        if arr[j][int(y)] == 0:
            arr[j][int(y)] = 1
        else:
            arr[j][int(y)] = 0

for i in range(19):
     print(*arr[i])

#ss = []
#for _ in range(n):
#    s = list(map(int, input().split())) # s = [1, 1]
#    ss.append(s) # ss = [[1, 1], [3, 3]]

#for i in range(19):
#    for j in range(19):
#         if [i, j] in ss:
#             for k in range(19):
#                 if arr[k][i] == 0:
#                     arr[k][i] = 1
#                 else:
#                     arr[k][i] = 0
#                 for l in range(19):
#                     if arr[j][l] == 0:
#                         arr[j][l] = 1
#                     else:
#                         arr[j][l] = 0 
# for i in range(19):
#     print(*arr[i])

