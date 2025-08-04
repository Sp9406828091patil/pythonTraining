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
    
    if methodologyToReplace == "FILL_WITH_MEDIAN" :
        median_value = df[columnLabel].median()
        df[columnLabel] = df[columnLabel].fillna(median_value)
        return df
    
    if methodologyToReplace == "FILL_WITH_MODE":
        mode_value = df[columnLabel].mode()
        df[columnLabel] = df[columnLabel].fillna(mode_value[0])
        return df
    
    if methodologyToReplace == "FILL_WITH_MEAN":
        mean_value = df[columnLabel].mean()
        df[columnLabel] = df[columnLabel].fillna(mean_value)
        return df
    
    if methodologyToReplace == "FILL_WITH_FORWARD_FILL":
        df[columnLabel] = df[columnLabel].fillna(method='ffill')
        return df
    
    if methodologyToReplace == "FILL_WITH_BACKWARD_FILL":
        df[columnLabel] = df[columnLabel].fillna(method='bfill')
        return df
    
    if methodologyToReplace == "FILL_WITH_INTERPOLATE":
        df[columnLabel] = df[columnLabel].interpolate(method='linear', limit_direction='both')
        return df