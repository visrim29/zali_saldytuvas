
from sub_paketas_product import product as produktas

class Recipe:
    ingredients = []
    instructions = []

    def __str__(self):
        return f"{self.ingredients}"

    def add_ingredient(self, product: produktas): # cia produktas pakeistas is Product
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id, new_quantity):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id):
        self.ingredients.pop(ingredient_id)