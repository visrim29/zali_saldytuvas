from fridge.fridge import Fridge
from recipe.recipe import Recipe
from product.product import Product

def main():
    fridge = Fridge()
    recipe = Recipe()
    while True:
        print("""Fridge\n0: exit\n1: add\n2: remove
3: check quantity\n4: print fridge\n5: check recipe
6: create recipe\n7: change product quantity in recipe
8: remove product from recipe\n9: peek recipe""")
        choice = input("Choose a number: ")
        if choice.startswith('0'):
            break
        elif choice.startswith('1'):
            name = input("Product: ")
            quantity = float(input("Quantity: "))
            fridge.add_product(name, quantity)
            fridge.check_product(name)
        elif choice.startswith('2'):
            name = input("Product: ")
            quantity = float(input("Quantity: "))
            fridge.remove_product(name, quantity)
            fridge.check_product(name)
        elif choice.startswith('3'):
            name = input("Product: ")
            quantity = float(input("Quantity: "))
            fridge.check_product_quantity(name, quantity)
        elif choice.startswith('4'):
            fridge.print_contents()
        elif choice.startswith('5'):
            fridge.check_recipe(recipe)
        elif choice.startswith('6'):
            ammount = int(input("Ammount of ingredients: "))
            for product in range(ammount):
                recipe.add_ingredient(Product(input("Product: "), float(input("Product quantity: "))))
        elif choice.startswith('7'):
            recipe.change_ingredient_quantity(int(input("Product: "))-1, float(input("Quantity :")))
        elif choice.startswith('8'):
            recipe.remove_ingredient(int(input("Product: "))-1)   
        elif choice.startswith('9'):
            print(recipe)
main()