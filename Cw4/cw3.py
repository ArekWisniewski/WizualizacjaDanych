lista=["Harnaś","Perła","Tyskie","Opa","Łomża","Romper","Stern"]
with open("DoZad3.txt", "w") as plik:
    for text in lista:
        plik.write(str(text)+"\n")
with open("DoZad3.txt", "r") as plik:
    for text in plik:
        print(text, end="")
