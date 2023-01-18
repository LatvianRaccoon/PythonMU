import copy

original = [['dogs', 'puppies'], ['cats', 'kittens']]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(['canines'])
print(original)
print('---------- Now look at the copied version ------------')
print(copied_outer_list)

original1 = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original1[:]
deeply_copied_version = copy.deepcopy(original1)
original1.append('Hi there')
original1[0].append(['marsupials'])
print('--------- Original ---------')
print(original1)
print('--------- Deep copy ---------')
print(deeply_copied_version)
print('--------- Shallow copy ---------')
print(shallow_copy_version)
