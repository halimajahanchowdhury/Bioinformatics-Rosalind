def hamming_distance(p, q):
    distance = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance


text = input().strip()
k, d = map(int, input().split())

patterns = [""]

for i in range(k):
    new_patterns = []

    for pattern in patterns:
        for base in "ACGT":
            new_patterns.append(pattern + base)

    patterns = new_patterns


counts = {}

for pattern in patterns:
    count = 0

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]

        if hamming_distance(pattern, kmer) <= d:
            count += 1

    counts[pattern] = count


max_count = max(counts.values())

for pattern in patterns:
    if counts[pattern] == max_count:
        print(pattern, end=" ")
