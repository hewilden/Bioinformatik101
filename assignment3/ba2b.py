#Median String

def FindHammingDistance(patternA, patternB):
    score = 0
    for base in range(len(patternA)):
        if patternA[base] != patternB[base]:
            score += 1
    return score

def DistanceBetweenPatternAndStrings(Pattern, DNA):
    k = len(Pattern)
    distance = 0
    for Sequence in DNA:
        HammingDistance = k+1
        for i in range(len(Sequence)-k+1):
            PatternB = Sequence[i:i+k]
            if HammingDistance > FindHammingDistance(Pattern, PatternB):
                HammingDistance = FindHammingDistance(Pattern, PatternB)
        distance += HammingDistance
    return distance

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

def DecToQuart(dec_number):
    quart_number = ""  # Erstelle Zahl (im string-Format) im System zur Basis 4 ("quart")
    while dec_number > 0:
        remainder = dec_number % 4
        dec_number = int(dec_number / 4)
        quart_number = str(remainder) + quart_number
    for i in range(k - len(quart_number)):
        quart_number = "0" + quart_number
    return quart_number


k = 6

fasta = "SampleDataset.txt"

fh = open(fasta, "r")
line = fh.readline()
DNA = []
while line:
    line = line.rstrip("\n")
    DNA.append(line)
    line = fh.readline()

#zum Test: dataset aus ba2h
#DNA = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

'''
Die Idee: für alle Existierenden kmere der länge k (generiert aus listenindex durch number to pattern)
=> Berechne Distance des Patterns zu den Strings
Suche niedrigsten Listeneintrag
Ausgabe: erneut Number to pattern des Listenidex!
'''

print(DNA)

kmer_distances= []
for i in range(4**k):
    kmer_distances.append(0)

for index in range(len(kmer_distances)):
    pattern = NumToPat(DecToQuart(index))
    #print(pattern, end=" ")
    distance = DistanceBetweenPatternAndStrings(pattern, DNA)
    #print(distance)
    kmer_distances[index] = distance

def indices(list, value):
    return [i for i,x in enumerate(list) if x==value] #liefert Liste
for i in indices(kmer_distances, min(kmer_distances)):
    print(NumToPat(DecToQuart(i)), kmer_distances[i])

