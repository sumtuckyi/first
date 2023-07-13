a, b, v = map(int, input().split())
point = 0
day = 0

while True:
    point += a
    if point >= v:
        break
    else:
        point = point - b
        day += 1
        continue

print(day)