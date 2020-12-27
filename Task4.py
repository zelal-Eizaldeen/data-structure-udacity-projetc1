"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telemarketers = []
    precentage_codes = []
    for record in calls:
        if record[0] not in telemarketers:
           if record[0].find('140') == 0:
               telemarketers.append(record[0])
    telemarketers.sort()
    print("These numbers could be telemarketers: ")
    print(*telemarketers, sep='\n')







    

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

