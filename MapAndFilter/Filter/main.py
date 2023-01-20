
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


print(keep_evens([3, 4, 6, 7, 0, 1]))


def keep_evens1(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)


print(keep_evens1([3, 4, 6, 7, 0, 1]))

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter(lambda word: 'w' in word, lst_check))
print(filter_testing)

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = list(filter(lambda word: 'o' in word, lst))
print(lst2)
