import os
from datetime import date
import pandas as pd


today = date.today()
pd.options.mode.chained_assignment = None

path = r'D:\Report Automation\R&R'
input_path = r'D:\Report Automation\R&R\Input'
output_path = r'D:\Report Automation\R&R\Output'

os.chdir(output_path)
os.getcwd()
