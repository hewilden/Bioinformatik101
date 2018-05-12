#Aufgabe Nr. 1 heaufigste kmer(e) in Sequenz

input_sequence = "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
k = 12
print("Input: ", input_sequence)
print("Laenge des kmer: ", k)
kmer_Dict = {}

for i in range(len(input_sequence)-k):
    kmer = (input_sequence[0+i:k+i])
#    if len(kmer)==k:                       #war zunaechst um kurze kmer-stuecken am Ende der Sequenz zu vermeiden
                                            #jetzt vermieden durch "-k" in Zeile 9
    if kmer in kmer_Dict:
        kmer_Dict[kmer] +=1            #Incrementierung um 1
    else:
        kmer_Dict[kmer]=1              #Wie wendet man .append auf dict an?

# optional: print("{}-mere und Haeufigkeit: {}".format(k, kmer_Dict)) #macht aus biologischer Sicht fuer k=1 und k=3 Sinn.
maximum_value = max(kmer_Dict.values())    #bei mehreren Maximalen keys: Auswahl nach dem hoechsten Value.
print("Haeufigste:",[kmer for kmer, frequency in kmer_Dict.items() if frequency == maximum_value]) #kann dieser Loop fuer bessere Runtime umgangen werden?
print("mit je", maximum_value, "mal.")

