
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
