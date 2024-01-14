import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path


def calculate_time_difference(csv_file):
    df = pd.read_csv(csv_file, encoding='latin1')
    df['Created Date/Time'] = pd.to_datetime(df['Created Date/Time'], dayfirst=True)
    df['Actual End'] = pd.to_datetime(df['Actual End'], dayfirst=True)

    df['Time Difference (hours)'] = (df['Actual End'] - df['Created Date/Time']).dt.total_seconds() / 3600
    df['Time Category'] = df['Time Difference (hours)'].apply(lambda x: 'Within 4 Hrs' if x <= 4 else 'Beyond 4 Hrs')
    return df


# Input File
csv_file = inputs+'\\SF_Data.csv'
prod = calculate_time_difference(csv_file)
# print(prod)

# Within 4 Hrs Service calls
# --------------------------------
# print('Within 4 Hrs Service Calls calculation Started')
SC = prod.drop(index=prod[prod['Type of Work'] != 'Service Call'].index)
within_4_hrs = SC[['EMP_ID', 'Time Category']]

within_4_hrs['Hour_Bucket_1'] = 1
within_4_hrs = within_4_hrs.groupby(by=['EMP_ID', 'Time Category'], as_index=False)['Hour_Bucket_1'].sum()
within_4_hrs['Within_4_Hrs_Per'] = 100 * within_4_hrs['Hour_Bucket_1'] / within_4_hrs.groupby('EMP_ID')[
    'Hour_Bucket_1'].transform('sum')
within_4_hrs1 = within_4_hrs.drop(index=within_4_hrs[within_4_hrs['Time Category'] != 'Within 4 Hrs'].index)
# print('Within 4 Hrs Service Calls calculation Completed')
#
# within_4_hrs1.to_csv(output + '\\within_4_hrs.csv')
