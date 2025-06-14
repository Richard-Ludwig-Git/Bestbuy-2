
class Product:
    """handles the key methods and init for the products"""
    def __init__(self, name=None, price=0, quantity=0):
        """construction parameter validation and initialisation"""
        self.name = name
        if name is None:
            raise Exception("Name is not allowed to be empty")
        self.price = price
        if price<0:
            raise Exception("Price could not be negative")
        self.quantity = quantity
        if quantity < 0:
            raise Exception("Quantity could not be negative")
        self.active = True


    def get_quantity(self):
        """getter for the quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity):
        """setter of the quantity of the product and activ change if 0"""
        self.quantity = quantity
        if quantity <= 0:
            self.active = False


    def is_active(self):
        """getter for the bool activ status of the product"""
        if self.active:
            return True
        else:
            return False


    def deactivate(self):
        """to deactivate the product by method"""
        self.active = False


    def activate(self):
        """to activate the product by method"""
        self.active = True


    def show(self):
        """simple print of name, price and quantity of the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """handle quantity and total price if product is bougth"""
        try:
            if self.quantity < int(quantity):
                raise Exception("Quantity to high, not enough in Stock")
            else:
                self.quantity -= int(quantity)
                return self.price * int(quantity)
        except ValueError:
            return "Sorry, wrong Value"