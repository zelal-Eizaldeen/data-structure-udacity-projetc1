"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    all_phone_nums = []
    area_codes = []
    precentage_codes = []
    for record in calls:
        all_phone_nums.extend([record[0], record[1]])
       
        if record[0] not in area_codes:
           if record[0].find('(080)') == 0 or record[0].find('7') == 0 or record[0].find('8') == 0 or record[0].find('9') == 0:
               area_codes.append(record[0])
        if record[1] not in area_codes:
            if record[1].find('(080)') == 0 or record[1].find('7') == 0 or record[1].find('8') == 0 or record[1].find('9') == 0:
                area_codes.append(record[1])
        if record[0].find('(080)') == 0 and record[1].find('(080)') == 0:
            precentage_codes.extend([record[0], record[1]])
            
    area_codes.sort()
    print("The numbers called by people in Bangalore have codes:")
    print(*area_codes, sep='\n')
    precentage = (len(precentage_codes) / len(all_phone_nums)) * 100
    precentage_decimal = format(precentage, '.2f')

    print(f"{precentage_decimal}% of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
    
          













"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
