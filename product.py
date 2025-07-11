import promotions


class Product:
    """handles the key methods and init for the products"""
    def __init__(self, name=None, price=0, quantity=0, promotion=None):
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
        self.promotion = promotion

    def get_quantity(self):
        """getter for the quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity):
        """setter of the quantity of the product and activ change if 0"""
        self.quantity = quantity
        if quantity <= 0:
            self.active = False


    def set_promotion(self, promo):
        self.promotion = promo


    def get_promotion(self):
        print(self.promotion.name)


    def set_no_promotion(self):
        self.promotion = None


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
        if self.promotion is not None:
            print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Current Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """handle quantity and total price if product is bougth"""
        try:
            if self.quantity < int(quantity):
                raise Exception("Quantity to high, not enough in Stock")
            if self.promotion is not None:
                self.quantity -= int(quantity)
                return self.promotion.apply_promotion(self.price, quantity)
            else:
                self.quantity -= int(quantity)
                return self.price * int(quantity)
        except ValueError:
            return "Sorry, wrong Value"


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """construction parameter validation and initialisation"""
        super().__init__(name, price)
        self.quantity = 0
        self.active = True


    def set_quantity(self, quantity):
        pass


    def show(self):
        """simple print of name, price and quantity of the product"""
        if promotions is not None:
            print(f"{self.name}, Price: {self.price}, Current Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: {self.price}")


    def buy(self, quantity):
        """handle quantity and total price if product is bougth"""
        try:
            if self.promotion is not None:
                self.quantity -= int(quantity)
                return self.promotion.apply_promotion(self.price, quantity)
            else:
                return self.price * int(quantity)
        except ValueError:
            return "Sorry, wrong Value"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum=1):
        """construction parameter validation and initialisation"""
        super().__init__(name, price, quantity)
        self.active = True
        self.maximum = 1


    def show(self):
        """simple print of name, price and quantity of the product"""
        if promotions is not None:
            print(f"{self.name}, Price: {self.price}, only applyed once, Current Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: {self.price}, only applyed once")

    def buy(self, quantity):
        """handle quantity and total price if product is bougth"""
        try:
            if self.quantity < int(quantity):
                raise Exception("Quantity to high, not enough in Stock")
            elif int(quantity) > self.maximum:
                raise Exception("Shipping only applys once")
            elif self.promotion is not None:
                self.quantity -= int(quantity)
                return self.promotion.apply_promotion(self.price, quantity)
            else:
                self.quantity -= 1
                return self.price
        except ValueError:
            return "Sorry, wrong Value"