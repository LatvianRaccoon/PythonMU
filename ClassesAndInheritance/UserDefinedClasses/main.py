class Point():
    def get_x(self):
        return self.x


point1 = Point()
point2 = Point()

point1.x = 5
point2.x = 10

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