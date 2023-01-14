
states = {'Minnesota': ['St. Paul', 'Minneapolis', 'Saint Cloud', 'Stillwater'],
          'Michigan': ['Ann Arbor', 'Traverse City', 'Lansing', 'Kalamazoo'],
          'Washington': ['Seattle', 'Tacoma', 'Olympia', 'Vancouver']}

print(sorted(states, key=lambda state: len(states[state][0])))


def s_cities_count(cities_list):
    ''' return a count of how many cities begin with "S"'''
    ct = 0
    for city in cities_list:
        if city[0] == 'S':
            ct += 1
    return ct


print(sorted(states, key=lambda state: s_cities_count(states[state])))


def s_cities_count_for_state(state):
    cities_list = states[state]
    return s_cities_count(cities_list)


print(sorted(states, key=s_cities_count_for_state))
