print("Hellp world!")

def main():
    print("Hello world!")

def dluga_nazwa_funkcji():
# dlugaNazwaFunkcji
# Guido van Rossum
# pep8 pep0008


# Ctrl + / - ustaw komentarz/usuń komentarz
#Shift + Alt + strzałka góra/dół
#łacuch znakó

imie = "Ala"
imie ='Ala ma kota'
print(type(imie))
<class 'str'>
imie = str("Ala") #poprzez konstruktor
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isin
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'None Type'>

print("Ala" + "ma kota.")
# print("Ala" + "ma" + 5 + "kotów.")  BŁĄD
print("Ala " + "ma " + str(5) + "kotów.".)
print(5)
ilsc_kotow =5
print("Ala " + "ma {} kotów.".format(ilosc_kotow))
print("Ala " + f"ma {ilosc_kotow} korów.")
print("Ala ma {1} {0} {2} kotów.".format(4, 5, 7))
liczba + 6.857564746
print(f"Liczba {liczba:.2f}") # 2 miejsca dziesięt

#http://pyformat.info

print(imie[0])
# imie[0]= "O" nie jest mutowalny
imie = imie.lower()
print(imie)

# liczby 
liczba = 1
liczbaf = 4.5 
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) # dzielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")

#lista

lista = []
lista2 = [1, 2, 3]
lista3 = [1, "Ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] # wartość 3, indeks 2
lista4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista4[1][1] # 5 

# słownik
slownik = {}
slownik2 = {"klucz": "wartość"}
slownik3 ={0: "Adam"}
slownik2["klucz"] = "cośtam"
slownik3 [0]
slownik2 