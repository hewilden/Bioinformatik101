# Number to Pattern
dec_number = int(input("Enter dec_number: "))
length = int(input("Enter length of Sequence: "))

quart_number = ""               #Erstelle Zahl (im string-Format) im System zur Basis 4 ("quart")
while dec_number > 0:
    remainder = dec_number % 4
    dec_number = int(dec_number / 4)
    quart_number = str(remainder) + quart_number

for i in range(length-len(quart_number)):   #Bei Pattern die mit A beginnen...
    quart_number = "0" + quart_number       #Deshalb mag ich das System mit A=1, C=2, G=3 und T=4 lieber!

print("Quart_Number: ", quart_number)

def NumToPat(pattern):
    quart_text = ""
    for i in range(len(pattern)):   # Notiz: i startet bei 0, geht bis len-1
        if pattern[i] == "0":       # in "" da quart_number ein string ist
            factor = "A"
        elif pattern[i] == "1":
            factor = "C"
        elif pattern[i] == "2":
            factor = "G"
        elif pattern[i] == "3":
            factor = "T"
        quart_text += factor
    return quart_text

print("Quart_Text: ", NumToPat(quart_number))





