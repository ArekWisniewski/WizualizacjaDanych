# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
# Program Generuje liczby podzielne przez 4.

a = 10
b = 50
listDiv = []
for x in range (a,b): #From a10 to b50
    if x % 4 == 0:
        listDiv += [x]

ListDivis.writelines(str(listDiv))

ListDivis.close()
