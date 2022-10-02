import csv
import random

# initializing dictionary + keys
jobDict = {}
jobDict["Job Class"] = []
jobDict["Percentage"] = []

# opening .csv file and reading it as a .DictReader object
# adding the job class and percentage to their appropriate slots in the dictionary
with open('occupations.csv') as f:
    r =  csv.DictReader(f)
    for row in r:
        # making sure the total percentage is not accounted for
        if (row['Job Class']!="Total"):
            jobDict["Job Class"].append(row['Job Class'])
            # making sure the percentage is a float, not a string
            jobDict["Percentage"].append(float(row['Percentage']))

# testing
### print(jobDict)

print(random.choices(jobDict["Job Class"], jobDict["Percentage"]))
