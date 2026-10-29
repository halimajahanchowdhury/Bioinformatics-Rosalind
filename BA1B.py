
text = input()
k = int(input())

counts = {}

for i in range(len(text) - k + 1):
    pattern = text[i:i + k]
    counts[pattern] = counts.get(pattern, 0) + 1

max_count = max(counts.values())

for pattern in counts:
    if counts[pattern] == max_count:
        print(pattern, end=" ")
