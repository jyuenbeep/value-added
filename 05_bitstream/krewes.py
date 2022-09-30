import random

krewes = {}

# with open('test.txt') as f:
#     s = f.readlines()

s = "2$$$jasmine$$$duck@@@2$$$jeffrey$$$ducky@@@8$$$daniel$$$bob"

ary = s.split("@@@")
plist = []

for i in range(len(ary)):
    ary[i] = ary[i].split("$$$")
    if plist.index(ary[i][0])!=-1:
        plist+=ary[i][0]

for num in plist:
    krewes[num] = []
    
for i in ary:
    krewes[i[0]] += [i[1], i[2]]

# rrow = (list(krewes.keys()))
# print(f"{rrow} : {rcol}")

print(krewes)
