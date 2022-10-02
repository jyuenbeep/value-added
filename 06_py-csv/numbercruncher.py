import csv
with open('occupations.csv') as f:
    r =  csv.DictReader(f)
    # for row in r:
    #     print(row)

print(r)
