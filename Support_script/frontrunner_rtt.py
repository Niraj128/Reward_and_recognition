import pandas as pd
import path_dir

inputs = path_dir.input_path
output = path_dir.output_path
directory = path_dir.path


# =========================
# Frontrunner RTT/RT
# =========================
# print('RTT/RT frontrunner calculation started')
rtt = pd.read_excel(inputs+'\\RTT_RT_Data.xlsx')
rtt['TAT%'] = (rtt['Close case count within 4 hour'] / rtt['Grand Total']).astype(float)


def eligible(c):
    if c['Grand Total'] >= 600:
        response = "Eligible"
    else:
        response = "Not Eligible"
    return response


rtt['Case Closure Eligibility'] = rtt.apply(eligible, axis=1)


def closure_wtg(c):
    if c['Grand Total'] >= 600:
        response = 0.5
    else:
        response = ((0.5 / 600) * c['Grand Total'])
    return response


rtt['Closure Wtg (50%)'] = rtt.apply(closure_wtg, axis=1)


def quality_wtg(c):
    if c['Call Quality'] >= 0.9:
        response = 0.25
    else:
        response = ((0.25 / 0.9) * c['Call Quality'])
    return response


rtt['Quality Wtg (25%)'] = rtt.apply(quality_wtg, axis=1)


def tat_wtg(c):
    if c['TAT%'] >= 0.95:
        response = 0.25
    else:
        response = ((0.25 / 0.95) * c['TAT%'])
    return response


rtt['Within TAT Wtg (25%)'] = rtt.apply(tat_wtg, axis=1)
rtt['Agg_Wtg'] = rtt['Closure Wtg (50%)'] + rtt['Within TAT Wtg (25%)'] + rtt['Quality Wtg (25%)']

# print('********************** Monthly Calculation done *********************************')
