def square(x):
    y = x * x
    return y


def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c


a = -5
b = 2
c = 10

result = sum_of_squares(a, b, c)
print(result)


def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)


def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d


def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far


print(most_common_letter('abbbbbbbbbbbbccccddddd'))


def mult(number):
    multiply = number * addit(number)
    return multiply


def addit(num):
    adding = num + 5
    return adding


print(mult(3))
