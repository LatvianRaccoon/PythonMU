
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] += 1

for key, value in letter_counts.items():
    print(key + ':', value)


sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1


stri = "what can I do"
char_d = {}

for char in stri:
    if char not in char_d:
        char_d[char] = 0
    char_d[char] += 1
print(char_d)
