
julia = ('Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta, Georgia')
# or equivalently
julia1 = 'Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta, Georgia'

print(julia[4])


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a


print(circleInfo(10))


lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []

for tup in lst_tups:
    t_check.append(tup[2])

print(t_check)

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []

for tup in tups:
    seconds.append(tup[1])

print(seconds)