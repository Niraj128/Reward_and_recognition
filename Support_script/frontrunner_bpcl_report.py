import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# BPCL Report Submission
# ----------------------------
# print('BPCL Report Submission within TAT Mapping Started')
BPCL_Report = pd.read_csv(inputs + '\\BPCL_Reports.csv', encoding='latin1')
BPCL_Report = BPCL_Report.drop(
    index=BPCL_Report[BPCL_Report['Billing Service report Final Remark'] != 'Received'].index)

BPCL_Report.EMP_ID = BPCL_Report.EMP_ID.astype(str)
BPCL_Report.EMP_ID = BPCL_Report.EMP_ID.str.strip()
BPCL_Report.EMP_ID = BPCL_Report.EMP_ID.str.lstrip()
BPCL_Report.EMP_ID = BPCL_Report.EMP_ID.str.rstrip()
BPCL_Report.EMP_ID = BPCL_Report.EMP_ID.str.upper()

BPCL_Report_1 = BPCL_Report[['Billing Service report Final Remark', 'EMP_ID', 'Ageing']]
BPCL_Report_1.rename(columns={'Billing Service report Final Remark': 'Final_Remarks'}, inplace=True)


def within_tat(c):
    if c['Ageing'] < 3:
        response = 1
    else:
        response = 0
    return response


BPCL_Report_1['Within_TAT'] = BPCL_Report_1.apply(within_tat, axis=1)


def total_report_count(c):
    if c.loc['Final_Remarks'] == "Received":
        response = 1
    else:
        response = 0
    return response


BPCL_Report_1['Total_Report_Count'] = BPCL_Report_1.apply(total_report_count, axis=1)
BPCL_Report_1['Received_Report_Per'] = 100 * BPCL_Report_1['Within_TAT'] / BPCL_Report_1.groupby('EMP_ID')[
    'Total_Report_Count'].transform('sum')
BPCL_Report_2 = BPCL_Report_1.groupby(by=['EMP_ID'], as_index=False)['Received_Report_Per'].sum()
# print('BPCL Report Submission within TAT Mapping Completed')
# BPCL_Report_2.to_csv(output + '\\BPCL_Report.csv')
