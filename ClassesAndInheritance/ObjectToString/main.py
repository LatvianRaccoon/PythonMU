class Point:

    def __init__(self, init_x, init_y):

        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return (self.x ** 2) + (self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x,
                     self.y - other.y)


p1 = Point(-2, 6)
p2 = Point(8, 9)
print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)

