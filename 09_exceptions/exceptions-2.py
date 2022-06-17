tuple1 = (1.25, False, "abc", 3, "qwerty123", 17, True, "a", 0.15, "ddos")
ind1 = int(input("Podaj index 0-9: "))
value1 = input(f"Podaj wartość do wymiany dla indeksu {ind1}: ")
try:
    tuple1[ind1] = value1
except TypeError:
    print("Got TypeError")


