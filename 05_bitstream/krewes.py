import random

krewes = {}

# with open('test.txt') as f:
#     s = f.readlines()

s = "2$$$jasmine$$$duck@@@2$$$jeffrey$$$ducky@@@8$$$daniel$$$bob"

ary = s.split("@@@")

# grabbing all the different periods from the array
for i in range(len(ary)):
    ary[i] = ary[i].split("$$$")
    if ary[i][0] not in krewes:
        krewes[ary[i][0]] = []
    
# appending each person to their specified key
for i in ary:
    krewes[i[0]].append([i[1], i[2]])

# rrow = (list(krewes.keys()))
# print(f"{rrow} : {rcol}")

print(krewes)
