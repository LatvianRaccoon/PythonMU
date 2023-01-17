
nested1 = [1, 2, ['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
for items in nested1:
    print('level1: ')
    if type(items) is list:
        for item in items:
            print('       level2: {}'.format(item))
    else:
        print(items)
