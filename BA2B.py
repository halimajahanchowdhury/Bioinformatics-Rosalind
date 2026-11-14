import itertools

def hamming_distance(p: str, q: str) -> int:
    """Calculates number of mismatches between two strings."""
    return sum(1 for a, b in zip(p, q) if a != b)


def distance_pattern_to_text(pattern: str, text: str, k: int) -> int:
    """Finds minimum Hamming distance between pattern and any k-mer in text."""
    min_dist = float('inf')
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        dist = hamming_distance(pattern, kmer)
        if dist < min_dist:
            min_dist = dist
            # Optimization: can't get better than 0 distance
            if min_dist == 0:
                break
    return min_dist


def distance_pattern_to_dna(pattern: str, dna: list[str], k: int) -> int:
    """Calculates sum of distances from pattern to all strings in DNA."""
    total_dist = 0
    for text in dna:
        total_dist += distance_pattern_to_text(pattern, text, k)
    return total_dist


def find_median_string(dna: list[str], k: int) -> str:
    """Finds a k-mer that minimizes the total distance to all strings in DNA."""
    best_pattern = ""
    min_total_distance = float('inf')

    # Generate all 4^k possible DNA k-mers (e.g. AAA, AAC, AAG, ... TTT)
    for chars in itertools.product('ACGT', repeat=k):
        pattern = "".join(chars)
        total_dist = distance_pattern_to_dna(pattern, dna, k)

        if total_dist < min_total_distance:
            min_total_distance = total_dist
            best_pattern = pattern

    return best_pattern


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

    # Handles inputs whether separated by newlines or spaces
    tokens = " ".join(lines).split()
    if tokens:
        k = int(tokens[0])
        dna = tokens[1:]

        result = find_median_string(dna, k)
        print(result)
