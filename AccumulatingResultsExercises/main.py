travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4,
          "Africa": 1, "Antarctica": 0, "Australia": 1}

total = 0
for continent in travel:
    total += travel[continent]
print(total)

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4,
            "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3,
            "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4,
            "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4,
            "ANTHRO 101": 4}

total_credits = 0
for course in schedule:
    total_credits += schedule[course]
print(total_credits)

d = {'a': 194, 'b': 54, 'c': 34, 'd': 44, 'e': 312, 'full': 31}

ks = list(d.keys())
best_key_so_far = ks[0]
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

placement = """Beaches are cool places to visit in spring however the Mackinaw 
            Bridge is near. Most people visit Mackinaw later since the island is a cool 
            place to explore."""

d = {}

for char in placement:
    if char not in d:
        d[char] = 0
    d[char] += 1

keys = list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)

product = "iphone and android phones"
lett_d = {}

for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] += 1

keys2 = list(lett_d.keys())
max_value = keys2[0]

for key in keys2:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print(max_value)
