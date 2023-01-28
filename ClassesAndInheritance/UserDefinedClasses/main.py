class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x


point1 = Point(5, 10)
point2 = Point(1, 5)

print(point1.get_x())
print(point2.get_x())


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0


p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")
print(p)
print(q)

print(p is q)


class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


t = NumberSet(6, 10)