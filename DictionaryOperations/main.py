
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

del inventory['pears']
print(inventory)

inventory['pears'] = 0
print(inventory)

inventory['bananas'] = inventory['bananas'] + 200
print(inventory)

numItems = len(inventory)
print(numItems)

swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}
swimmers['Phelps'] = swimmers['Phelps'] + 5
print(swimmers)
