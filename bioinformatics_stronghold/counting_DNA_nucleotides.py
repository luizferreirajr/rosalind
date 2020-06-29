"""
This program receives a DNA string and presents a group of four integers (separated by spaces)
counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

A = adenine
C = cytosine
G = guanine
T = thymine
"""

dna = input('Input your DNA string: ')
dna_index = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in dna:
    if i == 'A':
        dna_index['A'] = dna_index.get(i, 0) + 1
    elif i == 'C':
        dna_index['C'] = dna_index.get(i, 0) + 1
    elif i == 'G':
        dna_index['G'] = dna_index.get(i, 0) + 1
    elif i == 'T':
        dna_index['T'] = dna_index.get(i, 0) + 1


"""
Used the * at the beginning of dna_index to remove the dict structure
In other words, if I had use print (dna_index.values()) the program would present:
dict_values([20, 12, 17, 21])
"""
print(*dna_index.values())
