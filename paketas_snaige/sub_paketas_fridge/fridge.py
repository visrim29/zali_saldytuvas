
from sub_paketas_product import product as produktas
from sub_paketas_recipe import recipe as receptas

class Fridge:
    contents = []

    def check_product(self, product_name):
        for product_id,product in enumerate(self.contents):
            if product.name == product_name:
                return product_id,product
        return None, None
    
    def check_product_quantity(self, name:produktas, quantity:float):
        product_id, product = self.check_product(name)
        if product is not None and quantity <= product.quantity:
            return print(f"you have {product.quantity} {name} ")
        else:
            return print(f"you dont have {quantity} {name} you have {product.quantity}")
        
    def add_product(self, name, quantity:produktas):
        product_id, product = self.check_product(name)
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(produktas(name,quantity))

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
        
    def check_recipe(self, recipe:receptas):
        missing_product = []
        for ingredient in recipe.ingredients:
            product_id, product_fridge = self.check_product(ingredient.name)
            if  product_fridge is not None:
                missing_quantity = product_fridge.quantity - ingredient.quantity
                if missing_quantity < 0:
                    missing_product.append(produktas(ingredient.name, abs(missing_quantity)))
            else:
                missing_product.append(ingredient)
        if len(missing_product) == 0:
            print("You have the ingredients for the recipe")
        else:
            print(f"Missing products : {missing_product}")