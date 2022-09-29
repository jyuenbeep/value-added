import random

krewes = {}

# with open('test.txt') as f:
#     s = f.readlines()

s = "2$$$jasmine$$$duck@@@2$$$jeffrey$$$ducky@@@8$$$daniel$$$bob"

ary = s.split("@@@")

for i in range(len(ary)):
    ary[i] = ary[i].split("$$$")
    period = ary[i][0]
    krewes[period].update({ary[i][1]:ary[i][2]})

# rrow = (list(krewes.keys()))
# print(f"{rrow} : {rcol}")

print(krewes)
