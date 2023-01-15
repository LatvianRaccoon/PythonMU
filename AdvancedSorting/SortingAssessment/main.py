letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)

print(sorted_letters)

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter',
           'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

print(animals)

medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21, 'United States': 121, 'Germany': 42, 'China': 70}
alphabetical = sorted(medals)

print(medals)

medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21, 'United States': 121, 'Germany': 42, 'China': 70}
top_three = sorted(medals, key=lambda k: medals[k], reverse=True)
top_three = top_three[:3]

print(top_three)

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3,
             'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, key=lambda k: groceries[k], reverse=True)

print(most_needed)


def last_four(x):
    return str(x)[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)

print(sorted_ids)

sorted_id = sorted(ids, key=lambda item: str(item)[-4:])

print(sorted_id)

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda st: st[1])

print(lambda_sort)
