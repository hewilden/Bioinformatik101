#Aufgabe Nr. 1 mit faster frequent words
# hab ich was missverstanden, denn DIE LÖSUNG MIT DICT (Aufgabe 1) IST WESENTLICH SCHNELLER!!
sequence = "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
k = 12
if (k > len(sequence)):
    print("Error, k > Sequence!")
print("Input: ", sequence)
print("Laenge des kmer: ", k)

#Pattern To Number und Number To Pattern: (BA1M, BA1L)

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
    return dec_index # 1 = A, 2 = T, 5 = AA

def NumToPat(number):
    quart_text = ""
    for i in range(len((number))):   # Notiz: i startet bei 0, geht bis len-1
        if number[i] == "0":       # in "" da quart_number ein string ist
            factor = "A"
        elif number[i] == "1":
            factor = "C"
        elif number[i] == "2":
            factor = "G"
        elif number[i] == "3":
            factor = "T"
        quart_text += factor
    return quart_text

#Umrechnung von Dezimal zu Quartär:

def DecToQuart(dec_number):
    quart_number = ""  # Erstelle Zahl (im string-Format) im System zur Basis 4 ("quart")
    while dec_number > 0:
        remainder = dec_number % 4
        dec_number = int(dec_number / 4)
        quart_number = str(remainder) + quart_number
    return quart_number



#frequencies List: (BA1K)
kmer_frequencies = []
for i in range(4**k):               #an empty set
    kmer_frequencies.append(0)
# print(kmer_frequencies)

# kmer Häufigkeiten und abspeichern in Liste mit kmer-ListenIndex
for i in range(len(sequence)-k+1):
    pattern = sequence[i:i+k]
    if len(pattern) == k: #debug
        #print(pattern)
        list_index = PatToNum(pattern) #gibt decimal index
        for j in range(k):
            list_index -=  4**(k-j-1) #Abzug der Anzahl existierender n-mere mit n>k und -1 wegen Listenindex
        #print(list_index)
        kmer_frequencies[list_index] +=1


# maximum_value = max(kmer_frequencies)

def indices(list, value):
    return [i for i,x in enumerate(list) if x==value] #liefert Liste

print("most freuquent (listenindex): ", indices(kmer_frequencies, max(kmer_frequencies)))

#dann noch NumToPat(i) for i in indices #num to pat abändern, sodass es list_index=>decimal=>quart=>pattern!
for i in indices(kmer_frequencies, max(kmer_frequencies)):
    # for j in range(k):
    #     i += 4 ** (k - j -1)
    # print("i: ", i)
    quart_number = int(DecToQuart(i))
    for i in range(k - len(str(quart_number))):
        quart_number = "0" + str(quart_number)
    # print("QuartNumber: ", quart_number)
    print(NumToPat(str(quart_number)), end=" ")
print()
print("mit je", max(kmer_frequencies), "mal.")
