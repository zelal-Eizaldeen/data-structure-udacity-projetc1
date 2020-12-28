import csv
import numpy as np

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    all_phone_nums = set()
    for phone in texts:
       all_phone_nums.update([phone[0], phone[1]])
      
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for phone in calls:
        all_phone_nums.update([phone[0], phone[1]])
      #   if phone[0] not in unique_phone_numbers:
      #      unique_phone_numbers.append(phone[0])
      #   if phone[1] not in unique_phone_numbers:
      #      unique_phone_numbers.append(phone[1])
    print(f"There are {len(all_phone_nums)} different telephone numbers in the records. ")
  
    


