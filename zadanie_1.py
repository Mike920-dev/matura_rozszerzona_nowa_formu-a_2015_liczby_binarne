with open("liczby_binarne.txt", "r") as plik:
    ile_liczb = 0
    for liczba in plik:
        liczba = liczba.strip()
        zera = 0
        jedynki = 0
        for cyfra in liczba:
            if cyfra == "0":
                zera += 1
            elif cyfra == "1":
                jedynki += 1
        if zera > jedynki:
            ile_liczb += 1


print(ile_liczb)

with open("wynik4.txt", "w", encoding="UTF-8") as plik:
    plik.write("a) " + str(ile_liczb) + "\n")