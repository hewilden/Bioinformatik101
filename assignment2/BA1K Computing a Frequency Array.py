#Computing a Frequency Array
sequence = "ACGCGGCTCTGAAA"
k = 2
kmer_list = [] # liste mit 4^k Anzahlen für jedes kmer (in alphabetischer Reihenfolge der kmere) (k=2: AA, AC, AG, ...)
for i in range(4**k):
    kmer_list.append(0)
# für jedes kmer an stelle i übersetzen in Dezimal-Code (meine Lösung aus BA1L mit decimal index)
def PatToNum(pattern): #mit PatToNum aus BA1L
    dec_index = 0
    for i in range(len(pattern)):
        if pattern[i] == "A":
            factor = 0
        elif pattern[i] == "C":
            factor = 1
        elif pattern[i] == "G":
            factor = 2
        elif pattern[i] == "T":
            factor = 3
        dec_index += 4 ** (len(pattern) - 1 - i) * (factor + 1)  # fängt links an, mit 4^zahl der stelle
    return dec_index

#erstelle List Index => kmer-index in Liste ist (Dezimal-Code minus Anzahl kleinerer kmere und -1)
for i in range(len(sequence)):
    pattern = sequence[i:i+k]
    if len(pattern) == k:
        #print(pattern)
        list_index = PatToNum(pattern)
        for j in range(k):
            list_index -=  4**(k-j-1) #Abzug der Anzahl existierender n-mere mit n>k und -1 wegen Listenindex
        #print(list_index)
        kmer_list[list_index] +=1
for i in kmer_list:
    print(i, end=" ")
