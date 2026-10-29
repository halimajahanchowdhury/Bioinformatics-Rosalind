genome = input().strip()
k, L, t = map(int, input().split())

patterns = set()

for i in range(len(genome) - L + 1):
    window = genome[i:i + L]
    
    counts = {}
    
    for j in range(len(window) - k + 1):
        kmer = window[j:j + k]
        counts[kmer] = counts.get(kmer, 0) + 1
        
        if counts[kmer] >= t:
            patterns.add(kmer)

print(*patterns)