def mult(x, y=6):
    return x * y


print(mult(2))
print(mult(3, 5))
print(mult(4, 'hello'))


def sum1(intx, intz=5):
    return intz + intx


print(sum1(8, 2))
print(sum1(12))


def test(x, y=True, dict1={2: 3, 4: 5, 6: 8}):
    if y is True:
        for item in dict1.items():
            if x == item[0]:
                return item[1]
    return False


print(test(2))
print(test(4, False))
print(test(5, dict1={5: 4, 2: 1}))


def checkingIfIn(x, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction is True:
        for item in d.items():
            if x == item[0]:
                direction = True
                break
            else:
                direction = False
        return direction

    elif direction is False:
        for item in d.items():
            if x != item[0]:
                direction = True
            else:
                direction = False
                break
        return direction


print(checkingIfIn('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))


def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('Arthur')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('pear')
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('orange') + checkingIfIn('banana')

print(c_false)
print(c_true)
print(fruit_ans)
print(param_check)
