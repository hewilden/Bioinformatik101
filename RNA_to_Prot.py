print("This Program converts RNA-Sequence in Amino Acid Chain")

# sequence = input("Enter RNA-Sequence: ")

sequence = "AACGACUUAUAUAGUUGCUGGUCUAAGUAGUUGCGCGGGGGGUACCCUGCGCAAAAAUCUCCGUAGCGGUGGGCCGUUACUAAUCUAUCUGUAAAAAAAUGGCGGCGCCACUCUCUGCCUUCAGACUGGCAGUCGGGGCAUGUUUCAGCCGAGGACCACUCCAAAGUCGUGGAGGGCGCGGACAACUAAUGCGAGCUAAACGGGAAGGUCGUCGGUCGGCAACACGACCAACUCCAGCGCUUCU"
#sequence = input("Enter RNA: ")

codeDict = {"GGG":"G", "GGA":"G", "GGC":"G", "GGU":"G",
            "GAG":"E", "GAA":"E", "GAC":"D", "GAU":"D",
            "GCG":"A", "GCA":"A", "GCC":"A", "GCU":"A",
            "GUG":"V", "GUA":"V", "GUC":"V", "GUU":"V",
            "AGG":"R", "AGA":"R", "AGC":"S", "AGU":"S",
            "AAG":"K", "AAA":"K", "AAC":"N", "AAU":"N",
            "ACG":"T", "ACA":"T", "ACC":"T", "ACU":"T",
            "AUG":"M", "AUA":"I", "AUC":"I", "AUU":"I",
            "CGG":"R", "CGA":"R", "CGC":"R", "CGU":"R",
            "CAG":"Q", "CAA":"Q", "CAC":"H", "CAU":"H",
            "CCG":"P", "CCA":"P", "CCC":"P", "CCU":"P",
            "CUG":"L", "CUA":"L", "CUC":"L", "CUU":"L",
            "UGG":"W", "UGA":"Stop", "UGC": "C", "UGU": "C",
            "UAG":"Stop", "UAA":"Stop", "UAC":"Y", "UAU":"Y",
            "UCG":"S", "UCA":"S", "UCC":"S", "UCU":"S",
            "UUG":"L", "UUA":"L", "UUC":"F", "UUU":"F"}

# print(codeDict)

length = (len(sequence))
i = 0

print("Amino Acid Sequence: ", end="")
while (i < length-2):
    triplett = (sequence[i:i+3])
    if (codeDict[triplett] == "Stop"):
        break
    print(codeDict[triplett],end="")
    i=i+3
