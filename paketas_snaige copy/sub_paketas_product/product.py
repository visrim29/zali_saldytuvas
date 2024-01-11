
class Product:
    def __init__(self, name, quantity, **kwargs):
        self.name = name
        self.quantity = quantity
        self.unit_of_measurment = 'Unit'
        for key, value in kwargs.items():
            setattr(self,key,value)

    def __str__(self):
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self):
        return f"({self.name}, {self.quantity})"