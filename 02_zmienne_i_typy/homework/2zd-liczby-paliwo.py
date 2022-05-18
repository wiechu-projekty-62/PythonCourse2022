fuel_usage = int(input("Zużycie paliwa [l/100km]: "))
distance = int(input("Dystans [km]: "))
cena1l = int(input("Cena 1 l paliwa [zł]: "))
koszt = distance / 100 * fuel_usage * cena1l
print("Koszt wyprawy: ", round(koszt, 2), "pln")

