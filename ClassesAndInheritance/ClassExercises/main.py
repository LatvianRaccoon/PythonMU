
class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike('blue', 89.99)
testTwo = Bike('purple', 25.0)


class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def get_color(self):
        return self.apple_color

    def get_quantity(self):
        return self.apple_quantity

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)

    def increase(self):
        self.apple_quantity += 1


apples = AppleBasket('blue', 4)
print(apples)


class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def get_name(self):
        return self.name

    def get_amt(self):
        return self.amt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)


t1 = BankAccount('Bob', 100)