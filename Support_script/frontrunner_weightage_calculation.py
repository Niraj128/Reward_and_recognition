import pandas as pd
import path_dir
import frontrunner_within_4_hrs
import frontrunner_upi_txn
import frontrunnert_index_prod
import frontrunner_service_calls
import frontrunner_bpcl_report
import frontrunner_charge_collection
import frontrunner_de_installation
import frontrunner_ter_pickup
import Weightage

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path

# print('Weightage Calculation started')
within_4 = frontrunner_within_4_hrs.within_4_hrs1
upi = frontrunner_upi_txn.upi_1
ip = frontrunnert_index_prod.index_prod
sc_within_month = frontrunner_service_calls.Dep_Within_Month_3
bpcl_report = frontrunner_bpcl_report.BPCL_Report_2
charge_collect = frontrunner_charge_collection.collection3
di_field = frontrunner_de_installation.di_final
pickup_summary = frontrunner_ter_pickup.result

frontrunner_wtg = pd.merge(ip, within_4[['EMP_ID', 'Within_4_Hrs_Per']], on='EMP_ID', how='left')
frontrunner_wtg1 = pd.merge(frontrunner_wtg, upi[['EMP_ID', 'UPI_Txn_Per']], on='EMP_ID', how='left')
frontrunner_wtg2 = pd.merge(frontrunner_wtg1, sc_within_month[['EMP_ID', 'Ser_60_days_per']], on='EMP_ID', how='left')
frontrunner_wtg3 = pd.merge(frontrunner_wtg2, bpcl_report[['EMP_ID', 'Received_Report_Per']], on='EMP_ID', how='left')
frontrunner_wtg4 = pd.merge(frontrunner_wtg3, charge_collect[['EMP_ID', 'Collection_per']], on='EMP_ID', how='left')
frontrunner_wtg5 = pd.merge(frontrunner_wtg4, di_field[['EMP_ID', 'TAT']], on='EMP_ID', how='left')
frontrunner_wtg6 = pd.merge(frontrunner_wtg5, pickup_summary[['EMP_ID', 'Percentage']], on='EMP_ID', how='left')

# ****** Weightage Calculation *********

df = Weightage.calculate_response(frontrunner_wtg6, 'Within_4_Hrs_Per', 10, 75, 'Within_4_Wtg')
df = Weightage.calculate_response(frontrunner_wtg6, 'UPI_Txn_Per', 10, 90, 'UPI_Txn_Wtg')
df = Weightage.ser_wtg_response(frontrunner_wtg6, 'Ser_60_days_per', 10, 1, 'Ser_calls_within_60_Wtg')
df = Weightage.calculate_response(frontrunner_wtg6, 'Received_Report_Per', 10, 100, 'Received_Report_Wtg')
df = Weightage.calculate_response(frontrunner_wtg6, 'Collection_per', 20, 80, 'Collection_per_Wtg')
df = Weightage.calculate_response(frontrunner_wtg6, 'TAT', 20, 90, 'DI_wtg')
df = Weightage.calculate_response(frontrunner_wtg6, 'Percentage', 20, 90, 'Pickup_wtg')

frontrunner_wtg6['Within_4_Wtg'] = frontrunner_wtg6['Within_4_Wtg'].fillna(0)
frontrunner_wtg6['UPI_Txn_Wtg'] = frontrunner_wtg6['UPI_Txn_Wtg'].fillna(0)
frontrunner_wtg6['Ser_calls_within_60_Wtg'] = frontrunner_wtg6['Ser_calls_within_60_Wtg'].fillna(0)
frontrunner_wtg6['Received_Report_Wtg'] = frontrunner_wtg6['Received_Report_Wtg'].fillna(10)
frontrunner_wtg6['Collection_per_Wtg'] = frontrunner_wtg6['Collection_per_Wtg'].fillna(0)
frontrunner_wtg6['DI_wtg'] = frontrunner_wtg6['DI_wtg'].fillna(0)
frontrunner_wtg6['Pickup_wtg'] = frontrunner_wtg6['Pickup_wtg'].fillna(0)

frontrunner_wtg6['Agg_wtg'] = frontrunner_wtg6['Within_4_Wtg'] + frontrunner_wtg6['UPI_Txn_Wtg'] \
                              + frontrunner_wtg6['Ser_calls_within_60_Wtg'] + frontrunner_wtg6['Received_Report_Wtg'] \
                              + frontrunner_wtg6['Collection_per_Wtg'] + frontrunner_wtg6['DI_wtg'] + frontrunner_wtg6[
                                  'Pickup_wtg']
# print('Weightage Calculation compledted')
# frontrunner_wtg6.to_csv(output+'\\final_wtg.csv')
