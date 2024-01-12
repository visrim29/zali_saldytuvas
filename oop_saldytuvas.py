class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"

    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None

    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name)
        if product is not None:
            product.quantity -= quantity
        else:
            self.contents.remove(Product(name, quantity))

    def print_contents(self):
        print('Fridge Contents: ')
        for product in self.contents:
            print(f'{product.name}: {product.quantity}')

    def check_recipe(self, recipe:Recipe):
        print('Recipe: ')
        missing_product = []
        for product_recipe in recipe.ingredients:
            product_id, product_fridge = self.check_product(product_recipe.name)
            if  product_fridge is not None:
                missing_quantity = product_fridge.quantity - product_recipe.quantity
                if missing_quantity < 0:
                    missing_product.append(Product(product_recipe.name, missing_product))
            else:
                missing_product.append(product_recipe)
        if len(missing_product) == 0:
            print("Dinner come!")
        else:
            print(f"Missing ingredients: {missing_product}")

recipe = {}

def main():
    fridge = Fridge()
    recipe = Recipe()
    while True:
        print('===[ Fridge ]===')
        print('0: Exit')
        print('1: Add Product')
        print('2: Remove Product')
        print('3: Check Product')
        print('4: Check Product Quantity')
        print('5: Print Fridge Contents')
        print('6: Create Recipe')
        print('7: Check Recipe')
        choice = input('Choice: ')
        if choice.startswith('0'):
            break
        elif choice.startswith('1'):
            name = input('Product: ')
            quantity = float(input('Quantity: '))
            fridge.add_product(name, quantity)
        elif choice.startswith('2'):
            name = input('Product: ')
            quantity = float(input('Quantity: '))
            fridge.remove_product(name, quantity)
        elif choice.startswith('3'):
            product_name = input('Product Name: ')
            product_id, product = fridge.check_product(product_name)
            if product is not None:
                print(f'{product.name} is in the fridge')
            else:
                print(f'{product_name} is not in the fridge')
        elif choice.startswith('4'):
            name = input('Product: ')
            product_id, product = fridge.check_product(name)
            if product is not None:                
                print(f"{product.name}: {product.quantity}.")
            else:
                print(f"{name} is not in the fridge")
        elif choice.startswith('5'):
            fridge.print_contents()
        elif choice.startswith('6'):
            amount = int(input("Amount of ingredients: "))
            for product in range(amount):
                recipe.add_ingredient(Product(input("Product: "), float(input("Product quantity: "))))
        elif choice.startswith('7'):
            fridge.check_recipe(recipe)

main()