index, k = map(int, input().split())

pattern = ""

for i in range(k):
    remainder = index % 4

    if remainder == 0:
        pattern = "A" + pattern
    elif remainder == 1:
        pattern = "C" + pattern
    elif remainder == 2:
        pattern = "G" + pattern
    elif remainder == 3:
        pattern = "T" + pattern

    index = index // 4

print(pattern)