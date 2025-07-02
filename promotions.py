

class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, price, quantity):
        return price*quantity

class PercentDiscount(Promotion):
    def __init__(self, name, percent=100):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        return int(price * (1 - (self.percent / 100))* int(quantity))


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, price, quantity):
        if int(quantity)%2 == 0:
            return int((int(quantity))*(price*0.75))
        else:
            return int((int(quantity)-1)*(price*0.75))+price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, price, quantity):
        if int(quantity)%3 == 0:
            return int((int(quantity)-(int(quantity)/3))*price)
        if 0 < int(quantity)%3 < 3:
            return int((int(quantity)-1)*price)
        else:
            return int(int(quantity) * price)



