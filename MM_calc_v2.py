import os
import json

#Calculation for MM Criteria

"""
This is a calculation of MM to check if it is acceptable, Once it has gone through
the criteria, it will then start to go through the calculation for MM.
"""

#Load JSON Files to read

file_path_one: str = r'/Users/simonwhite/PycharmProjects/Calculations/JSON/JSON Datalog.json'
file_path_two: str = r'/Users/simonwhite/PycharmProjects/Calculations/JSON/JSON Input Test.json'

if os.path.exists(file_path_one) and os.path.exists(file_path_two):
    with open(file_path_one, 'r') as json_file_one:
        mm_one = json.load(json_file_one)
        print("MM One data: " + str(mm_one))
    with open(file_path_two, 'r') as json_file_two:
        mm_two = json.load(json_file_two)
        print("MM Two data: " + str(mm_two))

def criteria_one(data):
    mm_net_premium = data.get('mm_net_premium')
    if mm_net_premium is None:
        return "mm net premium is not found in JSON"
    if 350 >= mm_net_premium > 1500:
        return "criteria one passed"
    else:
        return "criteria one failed"
