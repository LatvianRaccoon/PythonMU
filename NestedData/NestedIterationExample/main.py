nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
print(output)

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
yellow = False
four = False
orange = False

if 'yellow' in lst[2]:
    yellow = True

if 4 in lst[1]:
    four = True

if 'orange' in lst[0]:
    orange = True

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]
test1 = False
test2 = False
test3 = False

if 'hola' in L:
    test1 = True
if [5, 8, 7] in L:
    test2 = True
if 6.6 in L[2]:
    test3 = True

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
          'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',
                                                  ['physics', 'chemistry', 'biology']]]}
data = False
twentyfour = False
whole = False
physics = False

print(nested.values())
print(nested.keys())
if 'data' in nested:
    data = True
if 24 in nested.values():
    twentyfour = True
if 'whole' not in nested['window']:
    whole = True
if 'physics' in nested:
    physics = True

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22, 'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29, 'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20, 'Germany': 13}}

london_gold = nested_d['London']['Great Britain']
print(london_gold)

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
          'diving': ['springboard', 'platform', 'synchronized'],
          'track': ['sprint', 'distance', 'jumps', 'throws'],
          'gymnastics': {'women': ['vault', 'floor', 'uneven bars', 'balance beam'],
                         'men': ['vault', 'parallel bars', 'floor', 'rings']}}
v1 = sports['swimming'][2]
v2 = sports['diving'][1]
v3 = sports['gymnastics']['women']
v4 = sports['gymnastics']['men'][-1]

print(v1)
print(v2)
print(v3)
print(v4)

US_count = []
for key, val in nested_d.items():
    for k, v in val.items():
        if k == 'USA':
            US_count.append(v)
print(US_count)

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'],
          ['sea green', 'cornflower', 'lavender', 'indigo'],
          ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []

for lst in l_of_l:
    third.append(lst[2])

print(third)

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
            ['Felix', 'Bolt', 'Gardner', 'Eaton'],
            ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []

for lst in athletes:
    for word in lst:
        if 't' in word:
            t.append(word)
        else:
            other.append(word)

print(t)
print(other)
