""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
biudzetas = {}

def prideti_pajamas():
    paskirtis = input("Įveskite pajamų paskirtį: ")
    suma = float(input("Įveskite pajamų sumą: "))
    if paskirtis in biudzetas:
        biudzetas[paskirtis] = biudzetas[paskirtis] + suma
    else:
        biudzetas[paskirtis] = suma

def prideti_islaidas():
    paskirtis = input("Įveskite išlaidų paskirtį: ")
    suma = float(input("Įveskite išlaidų sumą: "))
    if paskirtis in biudzetas:
        biudzetas[paskirtis] = biudzetas[paskirtis] - suma
    else:
        biudzetas[paskirtis] = -suma

def spausdinti_zurnala():
    print("Biudžeto žurnalas:")
    for paskirtis, suma in biudzetas.items():
        print(f"{paskirtis}: {suma}")

def skaiciuoti_balansa():
    balansas = sum(biudzetas.values())
    print(f"Biudžeto balansas: {balansas}")

# funkcijos
prideti_pajamas()
prideti_pajamas()
prideti_islaidas()
prideti_islaidas()

spausdinti_zurnala()
skaiciuoti_balansa()


