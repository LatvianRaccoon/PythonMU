def sublist(lst):
    new_lst = []
    item = 0
    while item < len(lst) and lst[item] != 5:
        new_lst.append(lst[item])
        item += 1
    return new_lst


print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print(sublist([5]))
print(sublist([8, 6, 5]))
print(sublist([1, 6, 2, 3, 9]))


def check_nums(lst):
    new_list = []
    item1 = 0
    while item1 < len(lst) and lst[item1] != 7:
        new_list.append(lst[item1])
        item1 += 1
    return new_list


print(check_nums([0, 2, 4, 9, 2, 3, 6, 8, 12, 14, 7, 9, 10, 8, 3]))
print(check_nums([9, 302, 4, 62, 78, 97, 10, 7, 8, 23, 53, 1]))
print(check_nums([7, 8, 3, 2, 4, 51]))
print(check_nums([1, 6, 2, 3, 9]))


def sublist1(lst):
    new_list1 = []
    valid_input = False
    start = 0
    while not valid_input:
        if lst[start] == 'STOP':
            valid_input = True
        else:
            new_list1.append(lst[start])
            start += 1

    return new_list1


print(sublist1(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']))
print(sublist1(['jackie', 'paul', 'STOP']))
print(sublist1(['STOP']))


def stop_at_z(lst):
    new_list2 = []
    item = 0
    valid_input = False
    while not valid_input:
        if lst[item] == 'z':
            valid_input = True
        else:
            new_list2.append(lst[item])
            item += 1
    return new_list2


print(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))
print(stop_at_z(['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze']))
print(stop_at_z(['z']))

sum1 = 0
lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
print(sum1)

item = 0
sum2 = 0
while item < len(lst):
    sum2 += lst[item]
    item += 1
print(sum2)


def beginning(lst):
    my_list = []
    valid_input = False
    item = 0
    while not valid_input:
        if lst[item] == 'bye' or item > 9:
            valid_input = True
        else:
            my_list.append(lst[item])
            item += 1
    return my_list


print(beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning',
                 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']))
print(beginning(['bye', 'no', 'yes', 'maybe', 'sorta']))
print(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat',
                 'facebook', 'social media']))


