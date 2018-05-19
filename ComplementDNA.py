print("This code converts DNA to RNA, complement DNA and RNA, reverse DNA and reverse complement DNA")

# sequence = input("Enter DNA-Sequence: ")

# sequence = "TTGCTGAATATATCANCGACCAGATTCATCAACGCGCCCCCCATGGGACGCGTTTTTAGAGGCATCGCCACCCGGCAATGATTAGATAGACATTTTTTTACCGCCGC"
sequence = input("Enter sequence: ")


#Complement Strand:
c_seq = ""
for base in range(len(sequence)):
    if (sequence[base]=="A"):
        c_base = "T"
    elif (sequence[base] == "T"):
        c_base = "A"
    elif (sequence[base] == "C"):
        c_base = "G"
    elif (sequence[base] == "G"):
        c_base = "C"
    c_seq+=(c_base)

#reverse complement DNA
rc_seq = ""
base = len(sequence)-1
while base in range(len(sequence)):
    if (sequence[base]=="A"):
        c_base = "T"
    elif (sequence[base] == "T"):
        c_base = "A"
    elif (sequence[base] == "C"):
        c_base = "G"
    elif (sequence[base] == "G"):
        c_base = "C"
    rc_seq += (c_base)
    base -=1

#Complement RNA:

comp_RNA_seq = ""
for base in range(len(sequence)):
    if (sequence[base]=="A"):
        c_base = "U"
    elif (sequence[base] == "T"):
        c_base = "A"
    elif (sequence[base] == "C"):
        c_base = "G"
    elif (sequence[base] == "G"):
        c_base = "C"
    comp_RNA_seq+=(c_base)

# RNA:

RNA_seq = ""
for base in range(len(sequence)):
    if (sequence[base]=="A"):
        c_base = "A"
    elif (sequence[base] == "T"):
        c_base = "U"
    elif (sequence[base] == "C"):
        c_base = "C"
    elif (sequence[base] == "G"):
        c_base = "G"
    RNA_seq+=(c_base)

print("Original Sequence:               ", sequence)
print("The complement DNA Strand is:    ", c_seq)
print("The reverse-comp DNA Strand is:  ", rc_seq)
print("The transkript RNA:              ", RNA_seq)
print("The complement RNA is:           ", comp_RNA_seq)
