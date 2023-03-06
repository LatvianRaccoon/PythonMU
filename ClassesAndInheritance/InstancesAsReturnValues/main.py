class Point:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(int(mx), int(my))

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)


p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)
print(mid)
print(mid.get_x())
print(mid.get_y())
