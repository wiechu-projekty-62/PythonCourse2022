import random

name = input("Podaj swoje imię graczu: ")

lrund = int(input("Podaj liczbę rund: "))
print("Podanie wyrazu koniec podczas wyboru kończy grę.\n")
finalscoreP = 0
finalscoreC = 0
for i in range(lrund):
    playerChoose = input("Wybierz kamień, nożyczki lub papier: ")
    if (playerChoose == "koniec"):
        break


    choose = ["kamień", "papier", "nożyczki"]
    computer = choose[random.randint(0, 2)]
    print("Komputer wybrał: ", computer)

    scorePlayer = 0
    scoreComputer = 0

    if (playerChoose == computer):
        print("remis")
    elif (playerChoose == "papier") and (computer == "kamień"):
        scorePlayer = scorePlayer + 1
        print("Wygrałeś/łaś " + name)
    elif (playerChoose == "kamień") and (computer == "papier"):
        scoreComputer = scoreComputer + 1
        print("Przegrałeś/łaś " + name)
    elif (playerChoose == "nożyczki") and (computer == "kamień"):
        scoreComputer = scoreComputer + 1
        print("Przegrałeś/łaś " + name)
    elif (playerChoose == "kamień") and (computer == "nożyczki"):
        scorePlayer = scorePlayer + 1
        print("Wygrałeś/łaś " + name)
    elif (playerChoose == "papier") and (computer == "nożyczki"):
        scoreComputer = scoreComputer + 1
        print("Przegrałeś/łaś " + name)
    elif (playerChoose == "nożyczki") and (computer == "papier"):
        scorePlayer = scorePlayer + 1
        print("Wygrałeś/łaś " + name)

    print("Masz ", scorePlayer, " punktów", " : ", "a komputer ma ", scoreComputer, ".")
    finalscoreC = finalscoreC + scoreComputer
    finalscoreP = finalscoreP + scorePlayer
if (playerChoose != "koniec"):
    print("\nMasz ", finalscoreP, " punktów", " , ", "a komputer ma", finalscoreC, f'po {lrund} rundach')
