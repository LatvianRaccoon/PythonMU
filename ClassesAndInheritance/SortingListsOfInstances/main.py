class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


fruit_list = [
    Fruit('Cherry', 10),
    Fruit('Apple', 5),
    Fruit('Blueberry', 20),
]


for fruit in sorted(fruit_list, key=Fruit.sort_priority):
    print(fruit.name)

for fruit in sorted(fruit_list, key=lambda x: x.sort_priority()):
    print(fruit.name)
