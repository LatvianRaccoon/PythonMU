
Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}

credits = 0

for course in Junior:
    credits += Junior[course]
print(credits)

str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1
print(freq)

s1 = "hello"
counts = {}

for char in s1:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1
print(counts)

str2 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}

words = str2.split()

for word in words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
print(freq_words)

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}

words2 = sent.split()

for word in words2:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
print(wrd_d)

sally = "sally sells sea shells by the sea shore"
characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1

char_list = list(characters.keys())
best_char = char_list[0]

for char in char_list:
    if characters[char] > characters[best_char]:
        best_char = char
print(best_char)

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1 = string1.lower()

letter_counts = {}
for char in string1:
    if char not in letter_counts:
        letter_counts[char] = 0
    letter_counts[char] += 1
print(letter_counts)

