dna = input().strip()

complement = dna.translate(str.maketrans("ACGT", "TGCA"))

print(complement[::-1])