things = [2, 5, 9]
your_list = [value * 2 for value in things]
print(your_list)


def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


print(keep_evens([3, 4, 6, 7, 0, 1]))


def keep_evens1(nums):
    new_list1 = filter(lambda num: num % 2 == 0, nums)
    return list(new_list1)


print(keep_evens1([5, 7, 2, 4, 3, 1]))

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [x for x in L if x > 10]
print(lst2)

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

inner_list = tester['info']
compri = [d['name'] for d in inner_list]

print(compri)
