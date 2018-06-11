#Distance between pattern and strings

Pattern = "AAA"
DNA = "TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"
DNA = DNA.split()

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

print(DistanceBetweenPatternAndStrings(Pattern, DNA))