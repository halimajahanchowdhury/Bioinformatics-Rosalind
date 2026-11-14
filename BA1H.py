def hamming_distance(p, q):
    distance = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance


pattern = input().strip()
text = input().strip()
d = int(input())

positions = []

for i in range(len(text) - len(pattern) + 1):
    substring = text[i:i + len(pattern)]

    if hamming_distance(pattern, substring) <= d:
        positions.append(str(i))

print(" ".join(positions))
