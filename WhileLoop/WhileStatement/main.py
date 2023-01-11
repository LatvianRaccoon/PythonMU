
def sumTo(aBound):
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum += aNumber
        aNumber += 1
    return theSum


print(sumTo(4))
print(sumTo(1000))

count = 0
eve_nums = []

while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count += 1

print(eve_nums)

myList = [0, 9, 4.5, 1, 7, 4, 8, 9, 3]
new_list = []


def stop_at_four(lst):
    item1 = 0
    while item1 < len(lst) and lst[item1] != 4:
        new_list.append(lst[item1])
        item1 += 1
    return new_list


print(stop_at_four(myList))

list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

item = 0
accum = 0
while item < len(list1):
    accum += list1[item]
    item += 1
print(accum)
