import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# Charge Collection (BPCL + Plutus)
# ----------------------------------
# print('Charge Collection (BPCL + Plutus) calculation Started')
collection = pd.read_csv(inputs + '\\Charges collection.csv', encoding='latin1')
collection1 = collection[['EMP_ID', 'Opportunity actual cost', 'Charges collection']]

# Charge Collection  % Mapping
collection1['Collection_per'] = 100 * collection1['Charges collection'] / collection1.groupby('EMP_ID')[
    'Opportunity actual cost'].transform('sum')
collection2 = collection1[['EMP_ID', 'Collection_per']]
collection3 = collection2.groupby(by=['EMP_ID'], as_index=False)['Collection_per'].sum()
# print('Charge Collection (BPCL + Plutus) calculation Completed')
# collection3.to_csv(output+'\\Charge_collection.csv')
