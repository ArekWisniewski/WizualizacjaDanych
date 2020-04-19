with open("DoZad3.txt", "w+") as plik:
    plik.write(str(print("List")))
    plik.write(str(print("Listaa")))

with open("DoZad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
