import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# UPI Transaction
# ---------------
# print('UPI Transaction Mapping Started')
upi = pd.read_csv(inputs + '\\UPI_Txn.csv', encoding='latin1')

upi['EMP_ID'] = upi['EMP_ID'].replace("T-2395", "T-2393")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-840", "15363")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-085", "15364")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-734", "15365")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-457", "15354")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-2219", "T-2441")
upi['EMP_ID'] = upi['EMP_ID'].replace("11258", "T-3280")
upi['EMP_ID'] = upi['EMP_ID'].replace("Rahman", "T-1939")
upi['EMP_ID'] = upi['EMP_ID'].replace("T 2503", "T-2503")
upi['EMP_ID'] = upi['EMP_ID'].replace("T 2095", "T-2095")
upi['EMP_ID'] = upi['EMP_ID'].replace("T -1861", "T-1861")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-629", "T-3433")
upi['EMP_ID'] = upi['EMP_ID'].replace("T- 2017", "T-2017")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-521", "15352")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-761", "15353")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-608", "16381")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-145", "16384")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-786", "16385")
upi['EMP_ID'] = upi['EMP_ID'].replace("T-5231", "T-5231")

upi_1 = upi[['EMP_ID', 'Deployment Count', 'Dep_UPI_Enabled', 'Service Count', 'Ser_UPI_Enabled']]
upi_1 = upi_1.replace(" -   ", 0)
upi_1['Total_calls'] = upi_1['Deployment Count'].astype(int) + upi_1['Service Count'].astype(int)
upi_1['Upi_Txn'] = upi_1['Dep_UPI_Enabled'].astype(int) + upi_1['Ser_UPI_Enabled'].astype(int)
upi_1['Txn_%'] = (upi_1['Upi_Txn'] / upi_1['Total_calls']) * 100
upi_1['Txn_%'] = upi_1['Txn_%'].fillna(0)

upi_1['duplicated_flag'] = upi_1['EMP_ID'].duplicated()
upi_1 = upi_1[upi_1.duplicated_flag == False]
upi_1 = upi_1.drop(['duplicated_flag'], axis=1)
upi_1.rename(columns={'Txn_%': 'UPI_Txn_Per'}, inplace=True)
# print('UPI Transaction Mapping Completed')
# upi_1.to_csv(output + '\\upi_Txn.csv')
