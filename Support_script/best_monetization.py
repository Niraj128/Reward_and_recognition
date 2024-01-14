import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path

# =========================
# Best Monetization Award
# =========================
# print("Best Monetization award winner calculation started")
monetization = pd.read_csv(inputs + '\\Monetization.csv', encoding='latin1')
Active_employee = pd.read_csv(inputs + '\\Active_Employee.csv', encoding='latin1')
monetization1 = monetization.fillna(0)

# Exception handling

monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-2395", "T-2393")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-840", "15363")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-085", "15364")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-734", "15365")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-457", "15354")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-2219", "T-2441")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("11258", "T-3280")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("Rahman", "T-1939")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T 2503", "T-2503")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T 2095", "T-2095")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T -1861", "T-1861")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-629", "T-3433")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T- 2017", "T-2017")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-521", "15352")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-761", "15353")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-608", "16381")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-145", "16384")
monetization1['EMP_ID'] = monetization1['EMP_ID'].replace("T-786", "16385")


def eligible(c):
    if c['Percentage'] >= 0.80:
        response = "Eligible"
    else:
        response = "Not Eligible"
    return response


monetization1['Eligibility'] = monetization1.apply(eligible, axis=1)

monetization2 = pd.merge(monetization1, Active_employee[['EMP_ID', 'Full Name']], how='left', on='EMP_ID')
monetization3 = pd.merge(monetization2, Active_employee[['EMP_ID', 'Team Leader / State Co-ordinator']], how='left',
                         on='EMP_ID')
monetization4 = pd.merge(monetization3, Active_employee[['EMP_ID', 'AM Name / State Head']], how='left', on='EMP_ID')
monetization5 = pd.merge(monetization4, Active_employee[['EMP_ID', 'Region']], how='left', on='EMP_ID')
monetization6 = monetization5[
    ['EMP_ID', 'Full Name', 'Team Leader / State Co-ordinator', 'AM Name / State Head', 'Region',
     ' Opportunity', ' Collection Done', 'Percentage', 'Eligibility']]
monetization7 = monetization6.sort_values(by=['Eligibility', ' Collection Done'], ascending=[True, False])

# print("Best Monetization award winner calculation Completed")
