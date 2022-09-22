"""
Jasmine Yuen
SoftDev
K04 -- Python program to randomly select an element from a dictionary
2022-09-22
time spent: 0.5
"""

import random

krewes = {
    2 : ["devo1", "devo2", "devo3"],
    7 : ["devo1", "devo2", "devo3"],
    8 : ["devo1", "devo2", "devo3"]
}

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")
