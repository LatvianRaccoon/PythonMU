list1 = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for item in list1:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

for x in sorted(d, key=lambda k: d[k], reverse=True):
    print('{} appears {} times'.format(x, d[x]))

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_keys = sorted(dictionary)

print(sorted_keys)

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3,
             'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
grocery_keys_sorted = sorted(groceries)

print(grocery_keys_sorted)

sorted_values = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)

print(sorted_values)