def double(y):
    y = 2 * y


def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"


y = 5
double(y)
print(y)

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)


def myfun(lst):
    lst = [1, 2, 3]


mylist = ['a', 'b']
myfun(mylist)
print(mylist)


def myfun(lst):
    del lst[0]


mylist = ['a', 'b']
myfun(mylist)
print(mylist)
