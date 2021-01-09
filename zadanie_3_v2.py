with open("slowa_2018.txt", "r", encoding="UTF-8") as plik:
    slowa = []
    for line in plik:
        slowa.append(line.split())

liczba_wierszy = 0

for slowo1, slowo2 in slowa:
    slowo1 = "".join(sorted(slowo1))
    slowo2 = "".join(sorted(slowo2))
    if slowo1 == slowo2:
        liczba_wierszy += 1

print(f'c) Liczba wierszy zawierających parę słów, gdzie jedno słowo jest anagramem drugiego: {liczba_wierszy}')
#print("c) Liczba wierszy zawierających parę słów, gdzie jedno słowo jest anagramem drugiego:", liczba_wierszy)

with open("wyniki6.txt", "a", encoding="UTF-8") as plik:
    plik.write("c) Liczba wierszy zawierających parę słów, gdzie jedno słowo jest anagramem drugiego: " + str(liczba_wierszy) + "\n")
