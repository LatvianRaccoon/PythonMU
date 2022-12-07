
f = open('scarlet.txt', 'r')
txt = f.read()

t_count = 0
s_count = 0
for char in txt:
    if char == 't':
        t_count += 1
    elif char == 's':
        s_count += 1
print('t:', str(t_count), 'occurrences')
print('s:', str(s_count), 'occurrences')

f = open('scarlet.txt', 'r')
txt = f.read()

x = {}
x['t'] = 0
x['s'] = 0

for char in txt:
    if char == 't':
        x[char] += 1
    elif char == 's':
        x[char] += 1
print('t:', str(x['t']), 'occurrences')
print('s:', str(x['s']), 'occurrences')

f = open('scarlet.txt', 'r')
txt = f.read()

dict = {}

for char in txt:
    if char not in dict:
        dict[char] = 0
    dict[char] += 1
print(dict)
