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
# Sukuriamas tuscias biudzeto zurnalas
biudzetas = {} # tuscias zodynas

def prideti_pajamas(paskirtis, suma):
    if paskirtis in biudzetas:
        biudzetas[paskirtis] += suma
    else:
        biudzetas[paskirtis] = suma

def prideti_islaidas(paskirtis, suma):
    if paskirtis in biudzetas:
        biudzetas[paskirtis] -= suma
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
prideti_pajamas("Atlyginimas", 1000)
prideti_pajamas("Alga", 500)
prideti_islaidas("Maistas", 300)
prideti_islaidas("Nuoma", 600)

spausdinti_zurnala()
skaiciuoti_balansa()
