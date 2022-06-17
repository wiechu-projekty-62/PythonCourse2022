def avg1(a,b,c,d,e):
    sr = (a+b+c+d+e)/5
    print("Średnia arytmetyczna podanych 5 liczb wynosi: ", sr)

try:
    a, b, c, d, e = [float(num) for num in input("Podaj pięć liczb po przecinku: ").split(",")]
    avg1(a, b, c, d, e)

except ValueError:
    with open('file1.txt', 'a') as f:
        f.write('ValueError ')
   



