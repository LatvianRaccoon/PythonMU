class Point:

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x,
                     self.y - other.y)


p1 = Point(-5, 10)
p2 = Point(15, 20)
print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)

