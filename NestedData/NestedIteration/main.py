
nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("       level2: ", y)

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'],
        ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for lst in info:
    last_names.append(lst[1])

print(last_names)

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'],
     ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []

for lst in L:
    for word in lst:
        if 'b' in word:
            b_strings.append(word)

print(b_strings)
