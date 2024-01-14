import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# ******************* Reading input file *******************

active_emp = pd.read_csv(inputs + '\\Active_Employee.csv')
ip = pd.read_excel(inputs + '\\Index_Productivity.xlsx')

# print('Index Productivity Mapping Started')
ip.rename(columns={'Avg Per Day Productivity (MTD)': 'Index_Productivity'}, inplace=True)
ip1 = ip[['EMP_ID', 'FSR Name', 'Regional_Name', 'State_Head', 'State_Coordinator', 'Index_Productivity']]

ip2 = pd.merge(ip1, active_emp[['EMP_ID', 'Base city']], on='EMP_ID', how='left')
ip3 = pd.merge(ip2, active_emp[['EMP_ID', 'Region']], on='EMP_ID', how='left')

metro_list = ['Delhi', 'Chennai', 'Bangalore', 'Mumbai', 'Hyderabad', 'Kolkata']


def metro(c):
    if c['Base city'] in metro_list:
        response = 'Metro'
    else:
        response = 'Non-Metro'
    return response


ip3['City_Category'] = ip3.apply(metro, axis=1)


def eligibility(c):
    if c['City_Category'] == 'Metro' and c['Index_Productivity'] >= 14:
        response = 'Eligible'
    elif c['City_Category'] == 'Non-Metro' and c['Index_Productivity'] >= 12:
        response = 'Eligible'
    else:
        response = 'Not Eligible'
    return response


ip3['IP_Eligibility'] = ip3.apply(eligibility, axis=True)
index_prod = ip3[['EMP_ID', 'FSR Name', 'State_Coordinator', 'State_Head', 'Regional_Name', 'Region', 'City_Category',
                  'Index_Productivity', 'IP_Eligibility']]
# print('Index Productivity Mapping completed')
#
# index_prod.to_csv(output + '\\index_prod.csv')
