def int_return(y):
    return y


num = 2
print(int_return(num))


def add(x):
    return x + 2


print(add(num))


def change(x):
    return "Hello " + x + "! Nice to meet you!"


name = "Arthur"
print(change(name))


def accum(lst):
    total = 0
    for num in lst:
        total += num
    return total


mylist = [1, 3, 5, 6]
print(accum(mylist))


def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"


print(length(mylist))


def divide(x):
    return x / 2


def total(y):
    return divide(y) + 6


print(total(num))
