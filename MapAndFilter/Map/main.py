
def double_stuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list


things = [2, 5, 9]
print(things)
things = double_stuff(things)
print(things)


def triple(value):
    return 3*value


def triple_stuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)


def quadruple_stuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)


things1 = [2, 5, 9]
things3 = triple_stuff(things1)
print(things3)
things4 = quadruple_stuff(things)
print(things4)

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map(lambda value: 2*value, lst))
print(greeting_doubled)

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map(lambda st: st.upper(), abbrevs))
print(abbrevs_upper)
