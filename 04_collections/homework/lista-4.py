n = int(input("Podaj parzystą ilość elementów listy: "))
lista1 = []
for i in range(n):
    j = input(f"{i} element listy: ")
    lista1.append(j)
print(lista1)
ind1 = int(len(lista1)/2) - 1
ind2 = ind1 + 1
if lista1[ind1] == lista1[ind2]:
    print("2 środkowe elementy są takie same")
else:
    print("2 środkowe elementy są różne od siebie")

