
class Point:

    printed_rep = "*"

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j + 1) % 10) + (' ' * (int(self.x) - 1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j + 1) % 10))
        rows.reverse()
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)
        return "\n".join(rows)


point_1 = Point(2, 3)
point_2 = Point(3, 12)
print(point_1.graph())
print()
print(point_2.graph())

