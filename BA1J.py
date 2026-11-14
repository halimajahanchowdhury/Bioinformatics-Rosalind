
def ReverseComplement(pattern):
    complement = ""

    for nucleotide in pattern:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'

    return complement[::-1]


def Neighbors(pattern, d):
    result = []

    def generate(index, mismatches, current):

        if mismatches > d:
            return

        if index == len(pattern):
            result.append(current)
            return

        for nucleotide in "ACGT":

            if nucleotide == pattern[index]:
                generate(index + 1, mismatches, current + nucleotide)

            elif mismatches < d:
                generate(index + 1, mismatches + 1, current + nucleotide)

    generate(0, 0, "")
    return result


def FrequentWordsWithMismatchesAndReverseComplements(Text, k, d):

    frequency = {}

    for i in range(len(Text) - k + 1):
        pattern = Text[i:i + k]

        neighbors = Neighbors(pattern, d)

        for neighbor in neighbors:
            if neighbor not in frequency:
                frequency[neighbor] = 0

            frequency[neighbor] += 1

    max_count = 0

    for pattern in frequency:
        reverse = ReverseComplement(pattern)
        total = frequency.get(pattern, 0) + frequency.get(reverse, 0)

        if total > max_count:
            max_count = total

    result = set()

    for pattern in frequency:
        reverse = ReverseComplement(pattern)
        total = frequency.get(pattern, 0) + frequency.get(reverse, 0)

        if total == max_count:
            result.add(pattern)
            result.add(reverse)

    print(*sorted(result))


# Take input from Rosalind
Text = input().strip()
k, d = input().split()

k = int(k)
d = int(d)

FrequentWordsWithMismatchesAndReverseComplements(Text, k, d)
