
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L5 = []
L6 = []
for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)

L4 = list(zip(L1, L2))
for x1, x2 in L4:
    L5.append(x1 + x2)

L6 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]

print(L4)
print(L5)
print(L6)

lst1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
lst2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

lst3 = [a1 + a2 for (a1, a2) in list(zip(lst1, lst2)) if a1 > 10 and a2 < 5]

print(lst3)