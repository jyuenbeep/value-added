import csv

# initializing dictionary + keys
jobDict = {}
jobDict["Job Class"] = []
jobDict["Percentage"] = []

# opening .csv file and reading it as a .DictReader object
# adding the job class and percentage to their appropriate slots in the dictionary
with open('occupations.csv') as f:
    r =  csv.DictReader(f)
    for row in r:
        jobDict["Job Class"].append(row['Job Class'])
        jobDict["Percentage"].append(row['Percentage'])

# testing
print(jobDict)
