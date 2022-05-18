czypalindrom = input("zdanie: ")
czypalindrom = czypalindrom.lower()
czypalindrom = czypalindrom.replace(' ', '')
revczypalindrom = czypalindrom[::-1]
print(czypalindrom == revczypalindrom)




