def f(x):
    return x - 1


print(f)
print(type(f))
print(f(3))

lf = lambda x: x - 1

print(lambda x: x - 1)
print(type(lf))
print(lf(3))


def last_char(s):
    return s[-1]


print(last_char('Hello'))

last_char1 = lambda s: s[-1]

print(last_char1('HELLO'))
