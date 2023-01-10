
julia = 'Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta, Georgia'

name, surname, birth_year, movie, movie_year, profession, birth_place, = julia


def add(x, y):
    return x + y


print(add(3, 4))
z = (5, 4)
print(add(*z))

d = {'k1': 3, 'k2': 7, 'k3': 'some other value'}

for k, v in d.items():
    print('key: {}, value: {}'.format(k, v))


pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
p_number = []

for k, v in pokemon.items():
    p_names.append(k)
    p_number.append(v)

print(p_names)
print(p_number)


track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3,
                      'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0,
                      '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []
for k in track_medal_counts.items():
    track_events.append(k[0])
print(track_events)
