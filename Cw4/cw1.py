# Liczby podzielne przez 4.

ListDivis = open("C:\\GitHub\\WizualizacjaDanych\\Cw4\\cw1.py\\LiczbyPodzielnePrzez4.txt","w+")

a = 10
b = 50
listDiv = []
for x in range (a,b): #From a10 to b50
    if x % 4 == 0:
        listDiv += [x]

ListDivis.writelines(str(listDiv))

ListDivis.close()
