def calculate_response(df, column_name, wtg, per, new_column):
    df[new_column] = df[column_name].apply(lambda x: int(wtg) if x >= per else x * (wtg / per))
    return df


def ser_wtg_response(df, column_name, wtg, per, new_column):
    df[new_column] = df[column_name].apply(lambda x: int(wtg) if x <= per else (wtg - (x / (100 - int(per)))))
    return df
