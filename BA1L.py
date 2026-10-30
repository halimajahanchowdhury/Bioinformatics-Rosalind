pattern = input().strip()

number = 0

for base in pattern:
    number = number * 4

    if base == "A":
        number += 0
    elif base == "C":
        number += 1
    elif base == "G":
        number += 2
    elif base == "T":
        number += 3

print(number)