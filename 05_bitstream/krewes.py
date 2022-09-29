import random

krewes = {}

with open('test.txt') as f:
    s = f.readlines()
    
ary = s.split("@@@")

for i in len(ary):
    ary[i] = ary[i].split("$$$")
    period = ary[i][0]
    #retreiving the period from the subarray
    krewes[period] = ary[i][1]:ary[i][2]

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")