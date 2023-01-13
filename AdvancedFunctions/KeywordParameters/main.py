initial = 7


def f(x, y=3, z=initial):
    return 'x, y, z, are: ' + str(x) + ', ' + str(y) + ', ' + str(z)


print(f(2))
print(f(2, 5))
print(f(2, 5, 8))
print(f(2, z=8))

names_scores = [("Jack", [67, 89, 91]), ("Emily", [72, 95, 42]), ("Taylor", [83, 92, 86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name, s1=scores[0], s2=scores[1], s3=scores[2]))

names = ["Jack", "Jill", "Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n, n, n, "say hello"))

names = ["Jack", "Jill", "Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n, "say hello"))


def multiply(x, mult_int=10):
    return x * mult_int


print(multiply('Hello', 3))
print(multiply('Goodbye'))


def waste(mar, var="Water", marble="type"):
    final_string = var + " " + marble + " " + mar
    return final_string


print(waste('Pokemon'))
