import csv
import numpy as np

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
   
    unique_phone_numbers = []
    for phone in texts:
        if phone[0] not in unique_phone_numbers:
           unique_phone_numbers.append(phone[0])
        if phone[1] not in unique_phone_numbers:
           unique_phone_numbers.append(phone[1])
   
          
   
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for phone in calls:
        if phone[0] not in unique_phone_numbers:
           unique_phone_numbers.append(phone[0])
        if phone[1] not in unique_phone_numbers:
           unique_phone_numbers.append(phone[1])
    print(f"There are {len(unique_phone_numbers)} different telephone numbers in the records. ")
  
    


