punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for x in punctuation_chars:
        for y in word:
            if x == y:
                word = word.replace(y, '')

    return word


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(sentences):
    count = 0
    sentences = strip_punctuation(sentences).lower().split()
    for word in sentences:
        for wrd in positive_words:
            if word == wrd:
                count += 1

    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(sentences):
    count = 0
    sentences = strip_punctuation(sentences).lower().split()
    for word in sentences:
        for wrd in negative_words:
            if word == wrd:
                count += 1

    return count


myfile = open("resulting_data.csv", "w")
myfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
myfile.write('\n')

open_file = open("project_twitter_data.csv", 'r')

lines = open_file.readlines()
header = lines[0]
field_names = header.strip().split(',')
for row in lines[1:]:
    val = row.strip().split(',')
    myfile.write(
        '{},{},{},{},{}'.format(val[1], val[2], get_pos(val[0]), get_neg(val[0]), get_pos(val[0]) - get_neg(val[0])))
    myfile.write('\n')

myfile.close()
