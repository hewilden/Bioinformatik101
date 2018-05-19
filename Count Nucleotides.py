#this short program counts nucleotides in DNA Sequence

sequence = input("Enter: sequence: ").strip()

for i in "ACGT":
    print (sequence.count(i), end=" ")

print()
for i in "ACGT":
    print(i, ":", sequence.count(i))