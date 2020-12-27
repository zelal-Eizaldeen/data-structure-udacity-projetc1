"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import numpy as np


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    phone_nums = {}
    for record in calls:
        if record[0] not in phone_nums:
           phone_nums[record[0]] = int(record[3])
        else:
           phone_nums[record[0]] += int(record[3])
        if record[1] not in phone_nums:
           phone_nums[record[1]] = int(record[3])
        else:
           phone_nums[record[1]] += int(record[3])
    longest_caller = max(phone_nums, key=phone_nums.get)
    longest_duration = max(phone_nums.values())
         
    print(f"{longest_caller} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")

  
    
