print ("Ucze sie")
print ("Pythona! :)")
print("count pryjmujewartoscstringu".count("na"))
len("Dorota")
print(len([1,2]))
print(len("Dorota Krygowska"))

def sum (day, month, year):
    return day + month + year
print(sum(28,6,2023))

def dane(imie, nazwisko):
    imie_nazwisko = imie + ' ' + nazwisko
    return imie_nazwisko.title()
print(dane('Dorota','Krygowska'))

def change_name(imie):
    return "Jakub"

def get_name(imie, nazwisko):
    imie = change_name(imie)
    imie_nazwisko = imie + " " + nazwisko
    return imie_nazwisko.title()

imie_nazwisko_otrzymane = get_name(imie = "kamil", nazwisko = "kowalski")
print(imie_nazwisko_otrzymane)

new_name = change_name("Kamil")
print(new_name)

lista_uczestnikow = ['Kamil']
def zaaktualizuj_liste_uczestnikow(ls, imie):
    ls.append(imie)
    return ls

#zaaktualizuj_liste_uczestnikow(lista_uczestnikow, "Dorota")
print(lista_uczestnikow)

uczestnicy = ["Dorota", "Kamil", "Karolina", "Magda", "Paulina"]
lista_uczestnikow = []
for uczestnik in uczestnicy:
    zaaktualizuj_liste_uczestnikow(lista_uczestnikow, uczestnik)
    #lista_uczestnikow.append(uczestnik)
    print(lista_uczestnikow)