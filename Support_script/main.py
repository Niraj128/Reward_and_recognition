# @author: Niraj Kumar
# Reward and Recognition 2023-24
# CM : CM-4405

if __name__ == '__main__':
    print('Frontrunner Calculation Started')

    import path_dir
    import pandas as pd
    import frontrunner_weightage_calculation
    import frontrunner_rtt
    import best_monetization
    output = path_dir.output_path

    with pd.ExcelWriter('Reward_and_Recognition.xlsx') as writer:
        frontrunner_weightage_calculation.df.to_excel(writer, index=False, sheet_name='Frontrunner_Field')
        frontrunner_rtt.rtt.to_excel(writer, index=False, sheet_name='Frontrunner_RTT')
        best_monetization.monetization7.to_excel(writer, index=False, sheet_name='Monetization')

    print('Frontrunner Calculation Completed')
