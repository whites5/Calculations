import os
import json

# Calculation for MM
"""
This calculation will calculate if MM is first acceptable, if it is acceptable
then the code will also start to calculate what the premium output should be
for MM.
"""

file_path_one = r"C:\Users\whites5\OneDrive - Hastings Insurance Services Ltd\Documents\Python\Calculations\JSON\JSON Datalog.json"
file_path_two = r"C:\Users\whites5\OneDrive - Hastings Insurance Services Ltd\Documents\Python\Calculations\JSON\JSON Input Test.json"

# Check if files exist
if not os.path.exists(file_path_one):
    print(f"File not found: {file_path_one}")
if not os.path.exists(file_path_two):
    print(f"File not found: {file_path_two}")

# Load JSON files if they exist
if os.path.exists(file_path_one) and os.path.exists(file_path_two):
    with open(file_path_one, 'r') as json_file_one:
        MM_one = json.load(json_file_one)
        print("MM_one data:", MM_one)  # Print the loaded JSON data
    with open(file_path_two, 'r') as json_file_two:
        MM_two = json.load(json_file_two)
        print("MM_two data:", MM_two)  # Print the loaded JSON data

# Define your criteria functions
def criteria_one(MM_net):
    if 350 <= MM_net < 1500:
        print('Premium Boundary')
        return True
    else:
        print('criteria 1 is acceptable')
        return False

def criteria_two(mileage):
    if mileage <= 20000:
        print('Mileage')
        return True
    else:
        print('criteria 2 is acceptable')
        return False

def criteria_three(NCD_Years, NCD_Entitlement, Group):
    if NCD_Years == 0 and Group <= 10:
        print('NCD & VG')
        return True
    elif NCD_Years > 0 and Group > 10:
        print('criteria 3 is acceptable')
        return False
    if NCD_Entitlement >= 1:
        print('NCD Type')
        return True
    return False

def criteria_four(Licence, Licence_Years):
    if Licence != 'F' and Licence_Years < 3:
        print('Licence')
        return True
    elif Licence == 'F' and Licence_Years >= 3:
        print('criteria 4 is acceptable')
        return False
    else:
        print('Licence')
        return False

def criteria_five(Occupation):
    if Occupation in ('U03', '42D', '34D', '220'):
        print('Occupation')
        return True
    else:
        print('criteria 5 is acceptable')
        return False

def criteria_six(Modification):
    if Modification >= 1:
        print('Modification')
        return True
    else:
        print('criteria 6 is acceptable')
        return False

# Process MM_one data
if isinstance(MM_one, list):
    for MM_lookup in MM_one:
        print("Processing entry:", MM_lookup)  # Debugging statement to see each entry being processed
        MM_net = MM_lookup.get("mm_net_premium")
        mileage = MM_lookup.get("Vehicle_AnnualMileage")
        if criteria_one(MM_net):
            criteria_two(mileage)
            criteria_three(MM_lookup.get("Ncd_ClaimedYears"), MM_lookup.get("Ncd_ClaimedEntitlementReason"), MM_lookup.get("vehicle1_group"))
            criteria_four(MM_lookup.get("Driver_LicenceType"), MM_lookup.get("Driver_LicenceDate"))
            criteria_five(MM_lookup.get("Occupation_Code"))
            criteria_six(MM_lookup.get("Vehicle_ModifiedInd"))

            MM_lookup = {
                "MM_net": MM_net,
                "mileage": MM_lookup.get("Vehicle_AnnualMileage"),
                "NCD_Years": MM_lookup.get("Ncd_ClaimedYears"),
                "NCD_Entitlement": MM_lookup.get("Ncd_ClaimedEntitlementReason"),
                "Group": MM_lookup.get("vehicle1_group"),
                "Licence": MM_lookup.get("Driver_LicenceType"),
                "Licence_Years": MM_lookup.get("Driver_LicenceDate"),
                "Occupation": MM_lookup.get("Occupation_Code"),
                "Modification": MM_lookup.get("Vehicle_ModifiedInd")
            }
            print(MM_lookup)
else:
    print("The JSON data in file_path_one is not a list. Please check the file content.")

# Process MM_two data
if isinstance(MM_two, list):
    for MM_lookup in MM_two:
        print("Processing entry:", MM_lookup)  # Debugging statement to see each entry being processed
        MM_net = MM_lookup.get("mm_net_premium")
        if criteria_one(MM_net):
            criteria_two(MM_lookup.get("Vehicle_AnnualMileage"))
            criteria_three(MM_lookup.get("Ncd_ClaimedYears"), MM_lookup.get("Ncd_ClaimedEntitlementReason"), MM_lookup.get("vehicle1_group"))
            criteria_four(MM_lookup.get("Driver_LicenceType"), MM_lookup.get("Driver_LicenceDate"))
            criteria_five(MM_lookup.get("Occupation_Code"))
            criteria_six(MM_lookup.get("Vehicle_ModifiedInd"))

            MM_lookup = {
                "MM_net": MM_net,
                "mileage": MM_lookup.get("Vehicle_AnnualMileage"),
                "NCD_Years": MM_lookup.get("Ncd_ClaimedYears"),
                "NCD_Entitlement": MM_lookup.get("Ncd_ClaimedEntitlementReason"),
                "Group": MM_lookup.get("vehicle1_group"),
                "Licence": MM_lookup.get("Driver_LicenceType"),
                "Licence_Years": MM_lookup.get("Driver_LicenceDate"),
                "Occupation": MM_lookup.get("Occupation_Code"),
                "Modification": MM_lookup.get("Vehicle_ModifiedInd")
            }
            print(MM_lookup)
else:
    print("The JSON data in file_path_two is not a list. Please check the file content.")