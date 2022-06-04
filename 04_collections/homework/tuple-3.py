krotka1 = (0,10,20,30,40,50,60,70,80,90)
user_liczba = int(input("Podaj dowolną liczbę całkowitą: "))
for x in krotka1:
    if x == user_liczba:
        print("Indeks liczby na krotce to: ",krotka1.index(x))
        break
if user_liczba not in krotka1:
    print("Indeks liczby na krotce to: ", "Nie ma takiej liczby na krotce")




