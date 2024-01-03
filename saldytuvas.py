""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""

# Ideda produktą
def prideti_produkta(saldytuve, produktas, kiekis):
    if produktas in saldytuve:
        saldytuve[produktas] += kiekis
    else:
        saldytuve[produktas] = kiekis
# Išmeta produktą
def isimti_produkta(saldytuve, produktas, kiekis):
    if produktas in saldytuve:
        if saldytuve[produktas] >= kiekis:
            saldytuve[produktas] -= kiekis
        else:
            print(f"Kieko nepakanka: {produktas}")
    else:
        print(f"Produktas nerastas: {produktas}")
# Patikrina produktų kiekį šaldytuve
def patikrinti_kieki(saldytuve, produktas, reik_kiekis):
    if produktas in saldytuve:
        return saldytuve[produktas] >= reik_kiekis
    else:
        return False
# Printina kas yra šaldytuve kai tikrinama vardotojo
def spausdinti_saldytuva(saldytuve):
    print("Šaldytuve yra: ")
    for produktas, kiekis in saldytuve.items():
        print(f"{produktas}: {kiekis}")
# Patikrina visą šaldytuvą
def patikrinti_saldytuva(saldytuve, vidus):
    sarasas = {}
    for produktas, reik_kiekis in vidus.items():
        if produktas in saldytuve:
            trukstantis_kiekis = reik_kiekis - saldytuve[produktas]
            if trukstantis_kiekis > 0:
                sarasas[produktas] = trukstantis_kiekis
        else:
            sarasas[produktas] = reik_kiekis

    if sarasas:
        print("Trūksta šių produktų: ")
        for produktas, trukstantis_kiekis in sarasas.items():
            print(f"{produktas}: {trukstantis_kiekis}")
    else:
        print("1")

saldytuve = {}

while True:
    print('===[ Šaldytuvas ]===')
    print('0: Išeiti')
    print('1: Pridėti produktą')
    print('2: Išimti produktą')
    print('3: Patikrinti kiekį šaldytuve')
    print('5: Išspausdinti šaldytuvo turinį')
    pasirinkimas = input('Pasirinkimas: ')
    if pasirinkimas.startswith('0'):
        break
    elif pasirinkimas.startswith('1'):
        prideti_produkta(saldytuve, input('Produktas: '), float(input('Kiekis: ')))
    elif pasirinkimas.startswith('2'):
        isimti_produkta(saldytuve, input('Produktas: '), float(input('Kiekis: ')))
    elif pasirinkimas.startswith('3'):
        produktas = input('Produktas: ')
        reik_kiekis = float(input("Reikiamas kiekis: "))
        if patikrinti_kieki(saldytuve, produktas, reik_kiekis):
            print(f"{produktas} yra pakankamai.")
        else:
            print(f"Trūksta {produktas} šaldytuve")
    elif pasirinkimas.startswith('5'):
        spausdinti_saldytuva(saldytuve)