import os
import json

#Calculation for MM Criteria

"""
This is a calculation of MM to check if it is acceptable, Once it has gone through
the criteria, it will then start to go through the calculation for MM.
"""

#Load JSON Files to read

file_path_one: str = r'C:\Users\whites5\OneDrive - Hastings Insurance Services Ltd\Documents\Python\Calculations\JSON\JSON Datalog.json'
file_path_two: str = r'C:\Users\whites5\OneDrive - Hastings Insurance Services Ltd\Documents\Python\Calculations\JSON\JSON Input Test.json'

if os.path.exists(file_path_one) and os.path.exists(file_path_two):
    with open(file_path_one, 'r') as json_file_one:
        mm_one = json.load(json_file_one)
    with open(file_path_two, 'r') as json_file_two:
        mm_two = json.load(json_file_two)

print(json.dump(mm_one))
print(json.dump(mm_two))