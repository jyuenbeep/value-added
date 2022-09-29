import random

krewes = {}

with open('test.txt') as f:
    s = f.readlines()
    
ary = s.split("@@@")

for i in len(ary):
    ary[i] = ary[i].split("$$$")
    for index in len(ary[i]):
        ary[i][index]

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")