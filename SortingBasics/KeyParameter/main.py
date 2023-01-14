
list1 = [1, 7, 4, -2, 3]


def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


print(absolute(3))
print(absolute(-119))

for z in list1:
    print(absolute(z))

list2 = sorted(list1, key=lambda x: absolute(x))
print(list2)

print(sorted(list1, reverse=True, key=absolute))


def absolute_update(y):
    print("--- figuring out what to write on the post-it note for " + str(y))
    if y >= 0:
        return y
    else:
        return -y


print('About to call sorted')
list3 = sorted(list1, key=absolute_update)
print('Finished execution of sorted')
print(list3)

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


def second_let(a):
    return a[1]


sorted_by_second_let = sorted(ex_lst, key=second_let)
print(sorted_by_second_let)


nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


def last_char(b):
    return b[-1]


nums_sorted = sorted(nums, reverse=True, key=last_char)
print(nums_sorted)

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda c: c[-1])
print(nums_sorted_lambda)
