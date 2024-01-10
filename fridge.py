class Product:
    def __init__(self, name, quantity, **kwargs):
        self.name = name
        self.quantity = quantity
        self.unit_of_measurment = 'unit' 
        for key, value in kwargs.items():
            setattr(self,key,value)

    def __str__(self):
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self):
        return f"({self.name}, {self.quantity})"
    

class Recipe:
    ingredients = []
    instructions = []

    def __str__(self):
        return f"{self.ingredients}"

    def add_ingredient(self, product: Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id, new_quantity):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name):
        for product_id,product in enumerate(self.contents):
            if product.name == product_name:
                return product_id,product
        return None, None
    
    def check_product_quantity(self, name:Product, quantity:float):
        product_id, product = self.check_product(name)
        if product is not None and quantity <= product.quantity:
            return print(f"you have {product.quantity} {name} ")
        else:
            return print(f"you dont have {quantity} {name} you have {product.quantity}")
        
    def add_product(self, name, quantity:Product):
        product_id, product = self.check_product(name)
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name,quantity))

    def remove_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name)
        if product == None or (product.quantity - quantity < 0):
            return False
        elif product.quantity - quantity == 0:
            self.contents.pop(product_id)
        else:
            product.quantity -= quantity
        return True
          
    def print_contents(self):
        for product in self.contents:
            print(f"{product}")
        
    def check_recipe(self, recipe:Recipe):
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
            print("You have the ingredients for the recipe")
        else:
            print(f"Lost products : {missing_product}")


def main():
    fridge = Fridge()
    recipe = Recipe()
    while True:
        print("Fridge\n0: exit\n1: add\n2: remove\n3: check quantity\n4: print fridge\n5: check recipe\n6: create recipe\n7: change product quantity in recipe\n8: remove product from recipe\n9: peek recipe")
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