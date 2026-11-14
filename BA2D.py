import sys

def create_profile(motifs, k):
    profile = {}

    for base in "ACGT":
        profile[base] = []

        for position in range(k):
            count = 0

            for motif in motifs:
                if motif[position] == base:
                    count += 1

            probability = count / len(motifs)
            profile[base].append(probability)

    return profile


def find_most_probable_kmer(text, k, profile):
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

    return best_kmer


def calculate_score(motifs, k):
    score = 0

    for position in range(k):
        counts = {}

        for base in "ACGT":
            counts[base] = 0

            for motif in motifs:
                if motif[position] == base:
                    counts[base] += 1

        most_common_count = max(counts.values())
        score += len(motifs) - most_common_count

    return score


def greedy_motif_search(dna, k, t):
    # Step 1: Default baseline: take the first k-mer of each sequence
    best_motifs = []
    for sequence in dna:
        best_motifs.append(sequence[:k])

    # Step 2: Try every k-mer in the first sequence as the seed motif
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]

        # Step 3: Greedily pick the best k-mer in the remaining sequences
        for j in range(1, t):
            profile = create_profile(motifs, k)
            motif = find_most_probable_kmer(dna[j], k, profile)
            motifs.append(motif)

        # Step 4: Keep the set with the lowest score
        if calculate_score(motifs, k) < calculate_score(best_motifs, k):
            best_motifs = motifs

    return best_motifs


if __name__ == "__main__":
    first_line = input().split()
    k = int(first_line[0])
    t = int(first_line[1])

    dna = []
    for _ in range(t):
        dna.append(input().strip())

    best_motifs = greedy_motif_search(dna, k, t)

    for motif in best_motifs:
        print(motif)
