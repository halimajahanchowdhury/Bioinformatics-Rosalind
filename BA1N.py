def get_neighbors(pattern: str, d: int) -> list[str]:
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = []

    def backtrack(index: int, current: list[str], mismatches: int):
        # Prune branches that have too many mismatches
        if mismatches > d:
            return

        # Base case: completed string
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


if __name__ == "__main__":
    pattern = input().strip()
    d = int(input().strip())

    result = get_neighbors(pattern, d)
    print("\n".join(result))