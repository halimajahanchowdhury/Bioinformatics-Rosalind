Text = input().strip()
k = int(input())

nucleotide = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}

frequency = [0] * (4 ** k)

for i in range(len(Text) - k + 1):

    number = 0

    for j in range(k):
        number = number * 4 + nucleotide[Text[i + j]]

    frequency[number] += 1

print(*frequency)
