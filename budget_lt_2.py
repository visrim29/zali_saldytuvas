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

    def prideti_pajamas(self, paskirtis, suma):
        if paskirtis in self.biudzetas:
            self.biudzetas[paskirtis] += suma
        else:
            self.biudzetas[paskirtis] = suma

    def prideti_islaidas(self, paskirtis, suma):
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
biudzetas = Biudzetas()
biudzetas.prideti_pajamas("Atlyginimas", 1000)
biudzetas.prideti_pajamas("Alga", 500)
biudzetas.prideti_islaidas("Maistas", 300)
biudzetas.prideti_islaidas("Nuoma", 600)

biudzetas.spausdinti_zurnala()
biudzetas.skaiciuoti_balansa()

