#Pattern to number
pattern = "AAA"

number = ""
dec_number = 0
dec_index = -1

for i in range(len(pattern)):  #i startet bei 0, geht bis len-1
    if pattern[i] == "A":
        factor = 0
    elif pattern[i] == "C":
        factor = 1
    elif pattern[i] == "G":
        factor = 2
    elif pattern[i] == "T":
        factor = 3
    number += (str(factor))        #nummer repräsentiert eine Base
    dec_number += 4**(len(pattern)-1-i) * (factor)
    dec_index += 4**(len(pattern)-1-i) * (factor+1)   #fängt links an, mit 4^zahl der stelle

print("DNA-Code: ", number)
print("Decimal number (Assignment 2): ", dec_number)
print()
print("Decimal index (in ordered List): ", dec_index)