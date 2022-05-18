ty = input("Tytuł książki: ")
ty = ty.capitalize()
au = input("Autor książki: ")
au = au.capitalize()
li = input("Liczba stron: ")
spr4_1 = ty.isalpha() and au.isalpha() and li.isdigit()
print(spr4_1)
book = ty + " " + au + " " + li
print(len(book))


