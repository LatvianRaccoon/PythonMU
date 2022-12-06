
fileref = open("olympics.txt", "r")
lines = fileref.read()
print(lines[:40])
fileref.close()

print("\n")
print("\n")

fileref = open("olympics.txt", "r")
# lines = fileref.readlines()
for line in fileref:
    print(line.strip())
fileref.close()

print("\n")
print("\n")

fileref = open("olympics.txt", "r")
lines = fileref.readlines()
print(len(lines))
fileref.close()
