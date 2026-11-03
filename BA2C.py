text = input().strip()
k = int(input())

profile = {}

for base in "ACGT":
    profile[base] = list(map(float, input().split()))

best_kmer = text[:k]
best_probability = -1

for i in range(len(text) - k + 1):
    kmer = text[i:i + k]
    probability = 1

    for position in range(k):
        base = kmer[position]
        probability *= profile[base][position]

    if probability > best_probability:
        best_probability = probability
        best_kmer = kmer

print(best_kmer)