import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path


# print('Service calls within 60 Days Mapping Started')
Dep_Within_Month = pd.read_csv(inputs+'\\Within_Month_Ser_Calls.csv', encoding='latin1')
Dep_Within_Month = Dep_Within_Month.drop(index=Dep_Within_Month[Dep_Within_Month['Type of Work'] != 'Deployment'].index)
Dep_Within_Month.rename(columns={'Work Order Line Item: Asset: POS ID': 'POS_ID'}, inplace=True)


def total_deployment(c):
    if c['Type of Work'] == 'Deployment':
        response = 1
    else:
        response = 0
    return response


Dep_Within_Month['Total_Deployment'] = Dep_Within_Month.apply(total_deployment, axis=1)
Dep_Within_Month.rename(columns={'Service Resource: Employee Code': 'EMP_ID'}, inplace=True)

Serv_Within_Month = pd.read_csv(inputs+'\\Within_Month_Ser_Calls.csv', encoding='latin1')
Serv_Within_Month_1 = Serv_Within_Month.drop(
    index=Serv_Within_Month[Serv_Within_Month['Type of Work'] != 'Service Call'].index)
Serv_Within_Month_1.rename(columns={'Work Order Line Item: Asset: POS ID': 'POS_ID'}, inplace=True)
Serv_Within_Month_2 = Serv_Within_Month_1.groupby(by=['POS_ID'], as_index=False)['Type of Work'].count()
Serv_Within_Month_2.rename(columns={'Type of Work': 'Ser_Call_Within_60_Days'}, inplace=True)

Dep_Within_Month_1 = pd.merge(Dep_Within_Month, Serv_Within_Month_2[['POS_ID', 'Ser_Call_Within_60_Days']], how='left',
                              on='POS_ID')
Dep_Within_Month_1.Ser_Call_Within_60_Days = Dep_Within_Month_1.Ser_Call_Within_60_Days.fillna(0)


def ser_60_days(c):
    if c['Ser_Call_Within_60_Days'] > 0:
        response = 1
    else:
        response = 0
    return response


Dep_Within_Month_1['Ser_60_Days'] = Dep_Within_Month_1.apply(ser_60_days, axis=1)
Dep_Within_Month_1 = Dep_Within_Month_1.drop('Ser_Call_Within_60_Days', axis=1)

# Service call within 60 days % Mapping
Dep_Within_Month_1['Ser_60_days_per'] = 100 * Dep_Within_Month_1['Ser_60_Days'] / Dep_Within_Month_1.groupby('EMP_ID')[
    'Total_Deployment'].transform('sum')
Dep_Within_Month_2 = Dep_Within_Month_1[['EMP_ID', 'Ser_60_days_per']]
Dep_Within_Month_3 = Dep_Within_Month_2.groupby(by=['EMP_ID'], as_index=False)['Ser_60_days_per'].sum()
# print('Service calls within 30 Days Mapping Completed')
# Dep_Within_Month_3.to_csv(output + '\\Dep_Within_Month.csv')
