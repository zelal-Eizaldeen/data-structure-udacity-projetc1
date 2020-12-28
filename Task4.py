"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    all_phone_numbers = set()
    send_text_numbers = set()
    receive_text_numbers = set()
    for record in texts:
        all_phone_numbers.update([record[0],record[1]])
        send_text_numbers.add(record[0])
        receive_text_numbers.add(record[1])
   
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    outgoing_calls = set()
    receiving_calls = set()
    telemarketers = set()
   
    for record in calls:
        all_phone_numbers.update([record[0],record[1]])
        outgoing_calls.add(record[0])
        receiving_calls.add(record[1])
    telemarketers = all_phone_numbers - send_text_numbers - receive_text_numbers - receiving_calls
    sorted_telemarketers = sorted(telemarketers)
    print("These numbers could be telemarketers: ")
    print(*sorted_telemarketers, sep='\n')







    

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

