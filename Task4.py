"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    non_telemarketers = set()
    for record in texts:
        non_telemarketers.update([record[0],record[1]])
   


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    outgoing = set()
    telemarketers = set()
   
    for record in calls:
        non_telemarketers.add(record[1])
        outgoing.add(record[0])
    telemarketers = non_telemarketers - outgoing
    sortes_telemarketers = sorted(telemarketers)
    print("These numbers could be telemarketers: ")
    print(*sortes_telemarketers, sep='\n')







    

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

