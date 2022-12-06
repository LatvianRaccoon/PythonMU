
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory['oranges'])

for key, value in inventory.items():
    print(key, value)

for key in inventory.keys():
    print(key, 'has the value', inventory[key])

keys = list(inventory.keys())
print(keys)

print(list(inventory.values()))
print(list(inventory.items()))

print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print('We have no bananas')


print(inventory.get('apples'))
print(inventory.get('cherries'))

print(inventory.get('cherries', 0))

total = 0
mydict = {'cat': 12, 'dog': 6, 'elephant': 23, 'bear': 20}
for key in mydict:
    if len(key) > 3:
        total += mydict[key]
print(total)

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
print(events)