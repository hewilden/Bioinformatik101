#This program gives all possible ORFs of a DNA Sequence

# fasta = input("Enter fasta file name: ")
fasta = "rosalind_orf-3.txt"
fh = open(fasta, "r")

line = fh.readline()
meta = ""       #Label of Sequence, starting with >
DNA_seq = ""   #Actual Sequence

while line:
    line = line.rstrip("\n")    #removes newline char
    if ">" in line:
        meta = line
    else:
        DNA_seq += line
    line = fh.readline()

print(meta)

# DNA_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
DNA_rc = ""

#compute the Reverse Complement Strand:
base = len(DNA_seq)-1
while base in range(len(DNA_seq)):
    if DNA_seq[base] == "A":
        c_base = "T"
    elif DNA_seq[base] == "C":
        c_base = "G"
    elif DNA_seq[base] == "G":
        c_base = "C"
    else:
        c_base = "A"
    DNA_rc += c_base
    base -= 1
print("DNA-Sequence: ")
print(DNA_seq)
print(DNA_rc)

#transcribe both to mRNAs:
RNA_seq = ""
RNA_rc = ""
def RNA_Transcript(sequence):
    RNA = ""
    for base in range(len(sequence)):
        if (sequence[base]=="A"):
            c_base = "A"
        elif (sequence[base] == "T"):
            c_base = "U"
        elif (sequence[base] == "C"):
            c_base = "C"
        elif (sequence[base] == "G"):
            c_base = "G"
        RNA +=(c_base)
    return RNA

RNA_seq = RNA_Transcript(DNA_seq)
RNA_rc = RNA_Transcript(DNA_rc)
print("RNA-Sequence: ")
print(RNA_seq)
print(RNA_rc)

#Find motif AUG:
def find_AUG(sequence):
    AUG = []
    for i in range(len(sequence)):
        if sequence[i:i+3] == "AUG":
            AUG.append(i)
    return AUG

print("Start RNA_seq: ", find_AUG(RNA_seq))
print("Start RNA_rc ", find_AUG(RNA_rc))
print()

#translate function
def translate(sequence, key):
    AA_Seq = ""
    codeDict = {"GGG": "G", "GGA": "G", "GGC": "G", "GGU": "G",
                "GAG": "E", "GAA": "E", "GAC": "D", "GAU": "D",
                "GCG": "A", "GCA": "A", "GCC": "A", "GCU": "A",
                "GUG": "V", "GUA": "V", "GUC": "V", "GUU": "V",
                "AGG": "R", "AGA": "R", "AGC": "S", "AGU": "S",
                "AAG": "K", "AAA": "K", "AAC": "N", "AAU": "N",
                "ACG": "T", "ACA": "T", "ACC": "T", "ACU": "T",
                "AUG": "M", "AUA": "I", "AUC": "I", "AUU": "I",
                "CGG": "R", "CGA": "R", "CGC": "R", "CGU": "R",
                "CAG": "Q", "CAA": "Q", "CAC": "H", "CAU": "H",
                "CCG": "P", "CCA": "P", "CCC": "P", "CCU": "P",
                "CUG": "L", "CUA": "L", "CUC": "L", "CUU": "L",
                "UGG": "W", "UGA": "Stop", "UGC": "C", "UGU": "C",
                "UAG": "Stop", "UAA": "Stop", "UAC": "Y", "UAU": "Y",
                "UCG": "S", "UCA": "S", "UCC": "S", "UCU": "S",
                "UUG": "L", "UUA": "L", "UUC": "F", "UUU": "F"}
    i = key
    while i in range(len(sequence)):
        triplett = (sequence[i:i + 3])
        #if codeDict[triplett] == "Stop":
         #   break
        if len(triplett ) == 3:
            AA_Seq += (codeDict[triplett])
        i = i + 3
    return AA_Seq


'''
print("Translations: ")
print(translate(RNA_seq, 0))
print(translate(RNA_seq, 1))
print(translate(RNA_seq, 2))
print(translate(RNA_rc, 0))
print(translate(RNA_rc, 1))
print(translate(RNA_rc, 2))
print()
'''

#definiere ORF als String       PROBLEM: Bereich M bis Ende der Sequenz, weil: Orf MUSS mit STOP enden!
                                    # => Lösung: Integriere "Stop" und sortiere andere aus!
def ORF(sequence, Start):
    ORF = ""
    codeDict = {"GGG": "G", "GGA": "G", "GGC": "G", "GGU": "G",
                "GAG": "E", "GAA": "E", "GAC": "D", "GAU": "D",
                "GCG": "A", "GCA": "A", "GCC": "A", "GCU": "A",
                "GUG": "V", "GUA": "V", "GUC": "V", "GUU": "V",
                "AGG": "R", "AGA": "R", "AGC": "S", "AGU": "S",
                "AAG": "K", "AAA": "K", "AAC": "N", "AAU": "N",
                "ACG": "T", "ACA": "T", "ACC": "T", "ACU": "T",
                "AUG": "M", "AUA": "I", "AUC": "I", "AUU": "I",
                "CGG": "R", "CGA": "R", "CGC": "R", "CGU": "R",
                "CAG": "Q", "CAA": "Q", "CAC": "H", "CAU": "H",
                "CCG": "P", "CCA": "P", "CCC": "P", "CCU": "P",
                "CUG": "L", "CUA": "L", "CUC": "L", "CUU": "L",
                "UGG": "W", "UGA": "Stop", "UGC": "C", "UGU": "C",
                "UAG": "Stop", "UAA": "Stop", "UAC": "Y", "UAU": "Y",
                "UCG": "S", "UCA": "S", "UCC": "S", "UCU": "S",
                "UUG": "L", "UUA": "L", "UUC": "F", "UUU": "F"}
    i = Start
    while i in range(Start, len(sequence)):
        triplett = (sequence[i:i + 3])
        if len(triplett) != 3:
            break
        elif codeDict[triplett] == "Stop":
            ORF += (codeDict[triplett])
            break
        ORF += (codeDict[triplett])
        i = i + 3
    return ORF          #orf is a defined AA Sequence STRING


# create list of orfs:
def give_ORFs(sequence):
    ORF_list = []
    for Start in find_AUG(sequence):
        if len(ORF(sequence, Start))>0:
            ORF_list.append(ORF(sequence, Start))   #fügt AA Sequence zur LISTE der ORF
    return ORF_list

ORF_seq = give_ORFs(RNA_seq)
ORF_rc = give_ORFs(RNA_rc)




all_ORFs = ORF_rc+ORF_seq

print("All ORFs: ", all_ORFs)

#remove duplicates and strip stop:
all_ORFs_final = []
for ORF in all_ORFs:
    if ORF.strip("Stop") in all_ORFs_final:
        pass
    else:
        if ORF[-4:] == "Stop":
            all_ORFs_final.append(ORF[0:len(ORF)-4])


print("all Orfs with a Stop: ", all_ORFs_final)

for i in all_ORFs_final:
    print(i)
