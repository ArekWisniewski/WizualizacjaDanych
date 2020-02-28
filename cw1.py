print('Hello world')

def main():
    pass  

#łańcuch znaków
imie = "Adam"
print (imie)
print(type(imie))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print(imie[2])
imie ="Damam"
imie = imie.lower()
print(imie)
wiek = 3000

# print(imie + " ma" +wiek + "lat.")

print(imie + " ma " + wiek.__str__() + " lat.")
print(imie + " ma " + str(wiek) + " lat.")
print("{} ma {} lat.".format(imie, wiek))
print("{0} ma {1} lat.".format(imie, wiek))

# f-string
print(f"{imie} ma {wiek} lat.")

#pyformat.info
liczba = 6.21376969
print(f"{liczba:.2f}")

 # typ liczbowy
liczba = 5
liczbaf = 5.6
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2) # dzielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

tekst = "2137"
liczba_z_tekstu = int(tekst, 16)
print(liczba_z_tekstu)

import math
pi = 3.15
from math import *
from math import pow , sqrt , pi
import math as m
# m.pow(2, 2)
print(m.pi)

# listy

lista = [] # pusta lista
lista2 = list() # pusta lista
lista3 = [1, 2, 3]
lista3 = [1, "Ala", True, None, [1, 2]]
lista3[1] = "Zosia"

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(macierz[1][1])
print(0.1 + 0.2 == 0.3)

# Decimal 
print(f"{0.1:.20f}")

lista = lista + lista3
lista += lista3

# słowniki

słownik = {}
słownik = dict()
słownik3 = {"Klucz": "Wartość"}
słownik3 ['Klucz']
słownik3 ['Klucz'] = 100

słownik3[0] = 999
print(słownik3)

słownik3.keys()
słownik3.values()
print(słownik3.items())

# dict_items([('Klucz', 100), (0,999)])