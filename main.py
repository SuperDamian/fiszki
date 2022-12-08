file = open('slowka.txt')
lines = file.readlines()

def usuwanie_spacji(text):
    return text.replace(" ", "")

slowa = []
odpowiedzi = []

indexa = 0

for a in lines:
    spacje = 0
    slowa.append("")

    for b in a:
        if b == " ":
            spacje += 1
        if spacje == 0 or spacje == 1:
            slowa[indexa] += b
        elif spacje == 2:
            spacje = 0
            break
    
    for c in a:
        if c == " ":
            spacje += 1
        if spacje == 3:
            odpowiedzi.append("")
            odpowiedzi[indexa] += c
        if spacje == 4 or c == "":
            break
    indexa += 1

for d in range(0, len(slowa)):
    slowo = slowa[d]
    odpowiedz = usuwanie_spacji(odpowiedzi[d]).strip() #słowa się zapisywały jakoś dziwnie ze spacjami i nowymi linijkami więc użyłem tu funkcji z internetu żeby je usunąc

    odpowiedz_uzytkownika = input(slowo + " - ")

    if odpowiedz_uzytkownika == odpowiedz:
        print("DOBRZE")
    else:
        print("ŹLE, PRAWIDŁOWA ODPOWIEDŹ TO: " + odpowiedz)