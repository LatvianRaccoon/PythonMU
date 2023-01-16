nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
nested1[0].append('z')
nested1[1].append('w')
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
for lst in nested1:
    print(lst)

y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

# write code to print the value associated with key 'c' in the second dictionary (90)
print(nested2[1]['c'])
# write code to print the value associated with key 'b' in the third dictionary
print(nested2[2]['b'])
# add a fourth dictionary add the end of the list; print something to check your work.
nested2.append({'a': 13})
print(nested2)
# change the value associated with 'c' in the third dictionary from "yes" to "no"; print something to check your work
nested2[2]['c'] = 'no'
print(nested2)

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1 = animals[1][0]
print(idx1)

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs',
        'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]
print(plant)

