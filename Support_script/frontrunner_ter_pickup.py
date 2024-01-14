import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# Terminal Pick-up TAT
# ---------------------
# print('Terminal Pick-up TAT calculation Started')
pickup = pd.read_csv(inputs + '\\Terminal_Pickup.csv', encoding='latin1')
pickup_1 = pickup[['Status', 'Base_city', 'State', 'State_Coordinator', 'State_Head', 'Regional_Name', 'Region',
                   'City_Category', 'Pine_Category_01', 'EMP_ID', 'Full_Name']]


def total_pickup(c):
    if c['Status'] == 'Completed':
        response = 1
    else:
        response = 0
    return response


pickup_1['Total_Pickup'] = pickup_1.apply(total_pickup, axis=1)
pickup_1['Total_assigned'] = 1
pickup_final = pickup_1[['EMP_ID', 'Total_Pickup', 'Total_assigned']]
result = pickup_1.groupby("EMP_ID").apply(
    lambda group: (group["Total_Pickup"] / group["Total_assigned"]).mean() * 100).reset_index(name="Percentage")
# print('Terminal Pick-up TAT calculation completed')
# result.to_csv(output + '\\Ter_pick-up.csv')
