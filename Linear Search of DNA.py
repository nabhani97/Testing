from enum import IntEnum
from typing import Tuple, List

# define types and variables


Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

DaysofWeek: IntEnum = IntEnum('DaysofWeek', ('Mon', 'Tue'))

myDay: DaysofWeek = DaysofWeek.Mon


Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

#Â our initial gene to search within
gene_str: str = "TGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTTACG"

# function definitions
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene

def linear_contains2(g, c) -> bool:
    for x in g:
        print (x)
        if x == c:
            return True
    return False

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        print (codon)
        if codon == key_codon:
            return True
    return False

# start logic

my_gene: Gene = string_to_gene(gene_str)

#print ( my_gene )

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print("First run")
print(linear_contains2(my_gene, acg))  # True
print("Second run")
print(linear_contains2(my_gene, gat))  # False