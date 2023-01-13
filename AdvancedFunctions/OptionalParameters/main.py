def f(a, lst=[]):
    lst.append(a)
    return lst


print(f(1))
print(f(2))
print(f(3))
print(f(4, ['Hello']))
print(f(5, ['Hello']))

initial = 7


def f(x, y=3, z=initial):
    return "x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z)


print(f(2))
print(f(2, 5))
print(f(2, 5, 8))


def str_mult(x, y=3):
    return x * y


print(str_mult('ha'))
print(str_mult('ha'))
print(str_mult('ha', 0))
