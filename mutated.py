from Bio import pairwise2
from Bio.pairwise2 import format_alignment

normal_p53 = (
    "SQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPL"
)

mutated_p53 = (
    "SQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPHAPTPAAPAPAPSWPL"
)

alignments = pairwise2.align.globalxx(normal_p53, normal_p53)

print(format_alignment(*alignments[0]))

# Comparing position by position
print("=== Comparing sequences ===")
for i, (a, b) in enumerate(zip(normal_p53, mutated_p53), start=1):
    if a != b:
        print(f"⚠️ Mutation detected at position {i} : {a} → {b}")



