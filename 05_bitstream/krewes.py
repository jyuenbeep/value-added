import random

krewes = {}

f = open("test.txt", "r")
s = f.read()
f.close()

ary = s.split("@@@")

# grabbing all the different periods from the array
for i in range(len(ary)):
    ary[i] = ary[i].split("$$$")
    if ary[i][0] not in krewes:
        krewes[ary[i][0]] = []
    
# appending each person to their specified key
for i in ary:
    krewes[i[0]].append([i[1], i[2]])

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")
