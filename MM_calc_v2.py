import os
import json
import datetime

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

 #to check if market model criteria one is passing or not       
def criteriaOne(mm_data):
    mm_premium = mm_data.get("HD", {}).get("mm_net_premium")
    #print(f"mm premium: {mm_premium}")
    if 350 <= mm_premium < 1500:
        return 'Acceptable'
    else: 
        return 'Not Acceptable'
    
print(criteriaOne(mm_one))

def criteriaTwo(mm_datatwo):
    pol_data_list = (
        mm_datatwo.get("requestPayload", {})
        .get("PolMessage", {})
        .get("PolData", [])
    )
    for pol_data in pol_data_list:
        vehicle = pol_data.get("Vehicle", {})
        mileage_dict = vehicle.get("Vehicle_AnnualMileage", {})
        mileage_val = mileage_dict.get("Val")
        if mileage_val is not None:
            try:
                mileage = float(mileage_val)
                if mileage <= 20000:
                    return 'Acceptable'
                else:
                    return None
            except ValueError:
                return None
    return None

results_two = criteriaTwo(mm_two)
if results_two == 'Acceptable':
    print(results_two)



def criteriaThree_a(mm_datathree_a):
    pol_data_list = (
        mm_datathree_a.get("requestPayload", {})
        .get("PolMessage", {})
        .get("PolData", []) 
    )
    for pol_data in pol_data_list:
        vehicle_NCD = pol_data.get("Vehicle", {})
        NCD = vehicle_NCD.get("Ncd", {})
        entitlement = NCD.get("Ncd_ClaimedEntitlementReason", {})
        entitlement_val = entitlement.get("Val")
        if entitlement_val is not None:
            try:
                ncd_entitlement = int(entitlement_val)
                if ncd_entitlement >= 1:
                    return 'Acceptable'
                else:
                    return None
            except ValueError:
                return None
    return None

results_three_a = criteriaThree_a(mm_two)
if results_three_a == 'Acceptable':
    print(results_three_a)

def criteriaThree_b(mm_datathree_b1,mm_datathree_b2):
    pol_data_list = (
        mm_datathree_b1.get("requestPayload", {})
        .get("PolMessage", {})
        .get("PolData", [])
    )

    vehicle_group = mm_datathree_b2.get("HD", {}).get("vehicle1_group")
    if vehicle_group is not None:
        try:
            group = int(vehicle_group)
            if group <= 10:
                return 'Acceptable'
            else:
                return None
        except ValueError:
            return None
  
    for pol_data in pol_data_list:
        vehicle = pol_data.get("Vehicle", {})
        NCD = vehicle.get("Ncd", {})
        entitlement = NCD.get("Ncd_ClaimedYears", {})
        entitlement_val = entitlement.get("Val")
        if entitlement_val is not None:
            try:
                ncd_entitlement = int(entitlement_val)
                if ncd_entitlement >= 1:
                    return 'Acceptable'
                else:
                    return None
            except ValueError:
                return None
    return None
 
results_three_b = criteriaThree_b(mm_two, mm_one)
if results_three_b == 'Acceptable':
    print(results_three_b)

def criteriaFour(mm_datafour):
    pol_data_list = (
        mm_datafour.get("requestPayload", {})
        .get("PolMessage", {})
        .get("PolData", []) 
    )

    for pol_data in pol_data_list:
        drivers = pol_data.get("Driver", {})
        if isinstance (drivers, dict):
            drivers = [drivers]
        for driver in drivers:
            licence_type = driver.get("Driver_LicenceType", {})
            licence_type_val = licence_type.get("Val")
            if licence_type_val is not None:
                if licence_type_val.lower() == "F":
                    return 'Acceptable'
                else:
                    return 'Not Acceptable'

    
    for pol_data in pol_data_list:
        driver_DOB = pol_data.get("Driver", {})
        dob = driver_DOB.get("Driver_DateOfBirth", {})
        dob_val = dob.get("Val")
    


    for pol_data in pol_data_list:
        driver_Licence = pol_data.get("Driver", {})
        licence_date= driver_Licence.get("Driver_LicenceDate", {})
        licence_date_val = licence_date.get("Val")
    
   

results_four= criteriaFour(mm_two)
if results_four == 'Acceptable':
    print(results_four)