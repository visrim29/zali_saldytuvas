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
class Biudzetas:
    def __init__(self):
        self.biudzetas = {}

    def prideti_pajamas(self):
        paskirtis = input("Įveskite pajamų paskirtį: ")
        suma = float(input("Įveskite pajamų sumą: "))
        if paskirtis in self.biudzetas:
            self.biudzetas[paskirtis] += suma
        else:
            self.biudzetas[paskirtis] = suma

    def prideti_islaidas(self):
        paskirtis = input("Įveskite išlaidų paskirtį: ")
        suma = float(input("Įveskite išlaidų sumą: "))
        if paskirtis in self.biudzetas:
            self.biudzetas[paskirtis] -= suma
        else:
            self.biudzetas[paskirtis] = -suma

    def spausdinti_zurnala(self):
        print("Biudžeto žurnalas:")
        for paskirtis, suma in self.biudzetas.items():
            print(f"{paskirtis}: {suma}")

    def skaiciuoti_balansa(self):
        balansas = sum(self.biudzetas.values())
        print(f"Biudžeto balansas: {balansas}")

# Demonstrate the functionality
biudzeto_objektas = Biudzetas()
biudzeto_objektas.prideti_pajamas()
biudzeto_objektas.prideti_pajamas()
biudzeto_objektas.prideti_islaidas()
biudzeto_objektas.prideti_islaidas()

biudzeto_objektas.spausdinti_zurnala()
biudzeto_objektas.skaiciuoti_balansa()


