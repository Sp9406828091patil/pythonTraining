# Eploratory data analysis
import pandas as pd

def getNullValueColumns(df):
    return df.columns[df.isnull().any()].tolist()

def replaceNullValue(df, columnLabel, methodologyToReplace):

    if methodologyToReplace == "DROP_NULL_VALUES":
        return df.dropna(subset = [columnLabel])
    
    if methodologyToReplace == "FILL_WITH_ZERO":
        df[columnLabel] = df[columnLabel].fillna(0)
        return df

    fill na with median, mode, mean
    fill na with forward fill, backwardfill
fill na with interpolate 