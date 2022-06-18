from io import UnsupportedOperation

try:
    # Otworzenie pliku data1.txt.
    idfile1 = open('data1.txt', 'r')

    # Odczytanie zawartości pliku.
    contents1 = idfile1.read()

    # Zamknięcie pliku data1.txt.
    idfile1.close()

except IOError:
    print('Wystąpił błąd podczas odczytu pliku - brak dostępu do pliku.')

try:
    # Otworzenie pliku data2.txt.
    idfile2 = open('data2.txt', 'w')

    # Odczytanie zawartości pliku data2.txt.
    contents2 = idfile2.read()

    # Zamknięcie pliku data2.txt.
    idfile2.close()

except UnsupportedOperation:
    print('Wystąpił błąd podczas odczytu pliku - plik nie jest do odczytu.')

try:
    with open("data3.txt", "x") as fh:
        fh.write("Dane testowe")

except FileExistsError:
    print('Wystąpił błąd podczas tworzenia pliku - plik już istnieje.')
