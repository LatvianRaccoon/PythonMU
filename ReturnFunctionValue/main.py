
def square(x):
    y = x * x
    return y


toSquare = 10
result = square(toSquare)
print('The result of {} squared is {}.'.format(toSquare, result))


def longer_than_five(list_of_names):
    for name in list_of_names:
        if len(name) > 5:
            return True
    return False


list1 = ['Sam', 'Tera', 'Sal', 'Amita']
list2 = ['Rey', 'Ayo', 'Lauren', 'Natalie']

print(longer_than_five(list1))
print(longer_than_five(list2))


def square(x):
    print("square")
    return x*x


def g(y):
    print("g")
    return y + 3


print(square(g(2)))

