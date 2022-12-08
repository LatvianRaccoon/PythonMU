
f = open('scarlet.txt', 'r')
txt = f.read()

letters_counts = {}
for char in txt:
    if char not in letters_counts:
        letters_counts[char] = 0
    letters_counts[char] += 1

for char in letters_counts:
    print("There are", letters_counts[char], "'", char, "'s")


f2 = open('scarlet2.txt', 'r')
txt2 = f2.read()

dict = {}
for char in txt2:
    if char not in dict:
        dict[char] = 0
    dict[char] += 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
                 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
                 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 8,
                 'y': 4, 'z': 10}

scrabble_score = 0
for char in dict:
    if char in letter_values:
        scrabble_score = scrabble_score + letter_values[char] * dict[char]
print(scrabble_score)

travel = {'North america': 2, 'Europe': 8, 'South America': 3, 'Asia': 4, 'Africa': 1,
          'Antarctica': 0, 'Australia': 1}
total = 0
for continent in travel:
    total += travel[continent]
print(total)

