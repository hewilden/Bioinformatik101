#Randomized Motif Search

import random

def FindHammingDistance(patternA, patternB):    #aus letzter Übung
    score = 0
    for base in range(len(patternA)):
        if patternA[base] != patternB[base]:
            score += 1
    return score

def FindConsensusSequence(Motifs):
    ConsensusSequence = ""
    Profile = FindProfile(Motifs)
    for base in range(k):
        BaseScores = []
        for score in Profile.values():
            BaseScores.append(score[base])
        ConsensusSequence += NumToPat(str(BaseScores.index(max(BaseScores))))
    return ConsensusSequence

def FindProfile(Motifs):    #gibt Consensusanteile nach Laplace, k&t sind gegeben
    Profile = {"A":[1/(t+4)]*k, "C":[1/(t+4)]*k,
            "G":[1/(t+4)]*k, "T":[1/(t+4)]*k}       # +4 ist der Pseudocount
    for string in Motifs:
        for i, base in enumerate(string):
            Profile[base][i] += 1/(t+4)
    return Profile

def Distance(Motifs): #s.a. ba2h, patterns hier motifs
    ConsensusSequence = FindConsensusSequence(Motifs)
    score = 0
    for string in Motifs:
        score += FindHammingDistance(ConsensusSequence, string)
    return score

def NumToPat(number):   #aus number to pattern
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

def FindMotifs(Profile, DNA):   #nicht 100% auf meinem Mist gewachsen
    Motifs = []
    best_matches = []
    for string in DNA:
        best_p = 0
        for i in range(len(string)-k+ 1):
            kmer = string[i:i+k]
            index_count = 0
            p = 1
            for base in kmer:
                p *= Profile[base][index_count]
                index_count +=1
            if p > best_p:
                best_p = p
                best_kmer = kmer
        best_matches.append(best_p)
        Motifs.append(best_kmer)
    return Motifs


def RandomizedMotifSearch(DNA, k, t):
    random_motifs = []
    for string in DNA:
        i = random.randint(0, len(string)-k)
        random_motifs.append(string[i:i+k])
    BestMotifs = random_motifs                         #analog rosalind-Pseudocode
    while True:
        Profile = FindProfile(BestMotifs)
        Motifs = FindMotifs(Profile, DNA)

        if Distance(Motifs) < Distance(BestMotifs):     #Refinement-Evolution
            BestMotifs = Motifs
        else:
            return BestMotifs

#import Data
DNA = []
fasta = "SampleDataset1.txt"
fh = open(fasta, "r")
line = fh.readline()
while line:
    line = line.rstrip("\n")
    DNA.append(line)
    line = fh.readline()

k = 8   #länge kmer
t = 5   #anzahl strings in DNA

#get Output
Distances = []
Motifs = []
for trials in range(0, 100):
    Distances.append(Distance(RandomizedMotifSearch(DNA, k, t)))
    Motifs.append(RandomizedMotifSearch(DNA, k, t))

def indices(list, value):
    return [i for i,x in enumerate(list) if x==value] #liefert Liste
for i in indices(Distances, min(Distances)):
    print(Motifs[i], Distances[i])