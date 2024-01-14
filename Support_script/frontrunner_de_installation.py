import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# De-installation TAT..
# --------------------------------
# print('De-installation TAT calculation Started')
prod = pd.read_csv(inputs + '\\SF_Data.csv', encoding='latin1')
prod.rename(columns={'Created Date/Time': 'Actual_Start'},inplace=True)
DI = prod.drop(index=prod[prod['Type of Work'] != 'De-Installation'].index)


def tat(c):
    start = c['Actual_Start']
    end = c['Actual End']

    response = pd.bdate_range(start, end, freq='C', weekmask='Mon Tue Wed Thu Fri Sat Sun', ).size
    response = max(0, response - 1)
    return response


DI['TAT'] = DI.apply(tat, axis=1)


def tat_summary(c):
    if (c['City_Category'] == "Base") and (c['TAT'] < 4):
        response = "TAT"
    elif (c['City_Category'] == "6 Metro") and (c['TAT'] < 4):
        response = "TAT"
    elif (c['City_Category'] == "Non Base") and (c['TAT'] < 8):
        response = "TAT"
    else:
        response = "BTAT"
    return response


DI['TAT_Summary'] = DI.apply(tat_summary, axis=1)

di_final = DI[['EMP_ID', 'TAT_Summary']]


def tat_summary_1(c):
    if c['TAT_Summary'] == 'TAT':
        response = 1
    else:
        response = 1
    return response


di_final['TAT_Summary_1'] = di_final.apply(tat_summary_1, axis=1)

di_final = di_final.groupby(by=['EMP_ID', 'TAT_Summary'], as_index=False)['TAT_Summary_1'].sum()
di_final['TAT'] = 100 * di_final['TAT_Summary_1'] / di_final.groupby('EMP_ID')[
    'TAT_Summary_1'].transform('sum')
di_final = di_final.drop(index=di_final[di_final['TAT_Summary'] != 'TAT'].index)
# print('De-installation TAT calculation completed')
# di_final.to_csv(output + '\\De-installation.csv')
