# fileName = "C:/Users/HP/OneDrive/Documents/pythonTraining/weatherstats_toronto_daily.csv"

import pandas as pd

df = pd.read_csv('weatherstats_toronto_daily.csv')
# print(df)

print(df.info())


median = df['max_low_temperature_forecast'].median()
mode = df['max_low_temperature_forecast'].mode()
mean = df['max_low_temperature_forecast'].mean()
std = df['max_low_temperature_forecast'].std()

for iColumnLabel in df.columns():
    mean = caculate(df, iColumnLabel, "MEAN")
    median = caculate(df, iColumnLabel, "MEDIAN")
    df[iColumnLabel].fillna(mean)


def caculate(DataFrame, columnLabel, paramToCalculate):

    if paramToCalculate == "MEDIAN":
        return df[columnLabel].median()
    
