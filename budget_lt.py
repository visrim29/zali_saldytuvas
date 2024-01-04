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
budget = {}

def budget_add(purpose, amount):
    if purpose in budget:
        budget[purpose] += amount
    else:
        budget[purpose] = amount

def budget_subtract(purpose, amount):
    if purpose in budget:
        budget[purpose] -= amount
    else:
        budget[purpose] = - amount

def income_expenses():
    for purpose, amount in budget.items():
        print(f'Paskirtis: {purpose} {amount}')

def budget_balance():
    balansas = sum(budget.values())
    print(f'Balansas: {balansas}$')

while True:
    print('===[ Biudžetas] ===')
    print('0: Išeiti iš programos')
    print('1: Pridėti pajamas')
    print('2: Pridėti išlaidas')
    print('3: Spausdinti pajamų/išlaidų žurnalą')
    print('4: Pajamų/išlaidų balansas')
    choice = input('Meniu pasirinkimas: ')
    if choice.startswith('0'):
        break
    elif choice.startswith('1'):
        purpose = input('Įveskite paskirtį: ')
        amount = float(input('Įveskite sumą: '))
        budget_add(purpose, amount)
    elif choice.startswith('2'):
        purpose = input('Įveskite paskirtį: ')
        amount = float(input('Įveskite sumą: '))
        budget_subtract(purpose, amount)
    elif choice.startswith('3'):
        income_expenses()
    elif choice.startswith('4'):
        budget_balance()