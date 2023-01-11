theSum = 0
x = -1

while x != 0:
    x = int(input('Next number to add up (Enter 0 if no more numbers): '))
    theSum += x

print(theSum)


def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer


response = get_yes_or_no('Do you like lima beans Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy')
else:
    print('Too bad. If cooked right, they are quite tasty')


def checkout():
    total = 0
    count = 0
    more_items = True
    while more_items:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count += 1
            total += price
            print('Subtotal: $', total)
        else:
            more_items = False
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)


checkout()
