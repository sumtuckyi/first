arr = [list(map(int, input().split())) for _ in range(10)]

current = arr[1][1]
arr[1][1] = 9
i = 1
j = 1
while True:
    if arr[i][j + 1] != 1: #오른쪽 탐색
        if arr[i][j + 1] == 2:
            arr[i][j + 1] = 9
            break
        else:
            arr[i][j + 1] = 9
            j += 1
            continue
    else: #아래쪽 탐색
        if arr[i + 1][j + 1] != 1: 
            if arr[i + 1][j + 1] == 2:
                arr[i][j + 1] = 9
                break
            else:
                arr[i + 1][j + 1] = 9
                i += 1
                continue
        else:
            break

for i in range(10):
    print(*arr[i])