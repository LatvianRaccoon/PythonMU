def hello2(s):
    print('Hello', s)
    print('Glad to meet you')


hello2('Iman')
hello2('Jackie')


def hello3(s, n):
    greeting = "Hello {} ".format(s)
    print(greeting * n)


hello3('Wei', 4)
hello3('', 1)
hello3('Kitty', 11)
