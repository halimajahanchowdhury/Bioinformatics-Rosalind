p = input().strip()
q = input().strip()

distance = 0

for i in range(len(p)):
    if p[i] != q[i]:
        distance += 1

print(distance)