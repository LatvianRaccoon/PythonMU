
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = list(map(lambda value: 'Fruit: ' + value, lst_check))
print(map_testing)

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda state: state[0] == 'B', countries))
print(b_countries)

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'),
          ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'),
          ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'),
          ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [t[1] for t in people]
print(first_names)

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [item * 2 for item in lst]
print(lst2)

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [student[0] for student in students if student[1] >= 70]
print(passed)

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda st: len(st[0]) > 3 and len(st[1]), zip(l1,l2)))
print(opposites)

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan',
           'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda',
           'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species, population))

endangered = [x[0] for x in pop_info if x[1] < 2500]
print(endangered)
