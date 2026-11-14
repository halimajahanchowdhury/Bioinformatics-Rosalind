def hamming_distance(p: str, q: str) -> int:
    """Returns the number of mismatches between two equal-length strings."""
    return sum(1 for a, b in zip(p, q) if a != b)


def get_neighbors(pattern: str, d: int) -> list[str]:
    """Generates all k-mers at Hamming distance at most d from pattern."""
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = []

    def backtrack(index: int, current: list[str], mismatches: int):
        if mismatches > d:
            return
        if index == len(pattern):
            neighbors.append("".join(current))
            return

        original_char = pattern[index]
        for char in nucleotides:
            current.append(char)
            backtrack(index + 1, current, mismatches + (1 if char != original_char else 0))
            current.pop()

    backtrack(0, [], 0)
    return neighbors


def has_approximate_match(pattern: str, text: str, k: int, d: int) -> bool:
    """Checks if `pattern` appears in `text` with at most `d` mismatches."""
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if hamming_distance(pattern, kmer) <= d:
            return True
    return False


def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    """Finds all (k, d)-motifs present in all DNA sequences."""
    candidate_motifs = set()

    # Step 1: Any valid motif MUST be a neighbor of at least one k-mer in dna[0]
    first_seq = dna[0]
    for i in range(len(first_seq) - k + 1):
        kmer = first_seq[i:i + k]
        # Generate all d-neighbors of this k-mer
        for neighbor in get_neighbors(kmer, d):
            candidate_motifs.add(neighbor)

    valid_motifs = []

    # Step 2: Verify which candidate appears in EVERY string in dna
    for candidate in candidate_motifs:
        in_all_strings = True
        for seq in dna:
            if not has_approximate_match(candidate, seq, k, d):
                in_all_strings = False
                break
        
        if in_all_strings:
            valid_motifs.append(candidate)

    return sorted(valid_motifs)


if __name__ == "__main__":
    # Reads input line-by-line until a blank line or EOF
    lines = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break

    if lines:
        first_line = lines[0].split()
        k = int(first_line[0])
        d = int(first_line[1])
        dna = lines[1:]

        result = motif_enumeration(dna, k, d)
        # Rosalind expects motifs separated by spaces
        print(" ".join(result))