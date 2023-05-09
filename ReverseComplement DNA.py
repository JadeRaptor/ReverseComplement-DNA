def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern


def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev


def Complement(Pattern):
    basepairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement


Pattern = "AAAACCCGGT"
print(Reverse(Pattern))
print(Complement(Pattern))

print(ReverseComplement(Pattern))