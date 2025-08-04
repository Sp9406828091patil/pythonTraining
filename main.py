from fetchData.readCsv import readCSV
from fetchData.performEDA import (getNullValueColumns, replaceNullValue)
import pandas as pd

# get data
filePath = r"data\cosmetics_sales_data.csv"
df = readCSV(filePath)
df.info()


df_numeric = df.copy()
df_numeric['Country_encoded'] = pd.Categorical(df['Country']).codes
df_numeric['Product_encoded'] = pd.Categorical(df['Product']).codes
df_numeric['SalesPerson_encoded'] = pd.Categorical(df['Sales Person']).codes
df_numeric['Date_ordinal'] = pd.Categorical(df['Date']).codes
# remove duplicates rows here 
numerical_columns = ['Amount ($)', 'Boxes Shipped', 'Country_encoded', 'Product_encoded', 'SalesPerson_encoded', 'Date_ordinal']
data_analysis = df_numeric[numerical_columns]


# numeric_columns = df.select_dtypes(exclude=['object']).columns.tolist()
# # get null value columns
# nullValueColumns = getNullValueColumns(df)
# common = list(set(nullValueColumns) & set(numeric_columns))
common = df.select_dtypes(include=['object']).columns.tolist()
# print("Columns with Null Values:", nullValueColumns)

# copies for each operation
# dfDropNa = df.copy()
# dfFillNaWithZero = df.copy()
# dfFillNaWithMedian = df.copy()
# dfFillNaWithMode = df.copy()
# dfFillNaWithMean = df.copy()
# dfFillNaWithForwardFill = df.copy()
# dfFillNaWithBackwardFill = df.copy()
# dfFillNaWithInterpolate = df.copy()

# drop na on particular column  -> drop na can't be put on entire dataframe or on each column -> it may leads to delete all rows
# dfDropNa = replaceNullValue(df, 'date', "DROP_NULL_VALUES")

# get updated
# remove the empty rows-
for iColumnLabel in common:
   
    # dfFillNaWithZero = replaceNullValue(df, iColumnLabel, "FILL_WITH_ZERO")
    # # fill with median -
    # dfFillNaWithMedian = replaceNullValue(df, iColumnLabel, "FILL_WITH_MEDIAN")
    # fill with mode -for icolumnLabel in nullValueColumns:
    if iColumnLabel != 'date':
        dfFillNaWithMode = replaceNullValue(df, iColumnLabel, "FILL_WITH_MODE")

# # fill with mean -
#     dfFillNaWithMean = replaceNullValue(df, iColumnLabel, "FILL_WITH_MEAN")

# # fill with forward fill
#     dfFillNaWithForwardFill = replaceNullValue(df, iColumnLabel, "FILL_WITH_FORWARD_FILL")

# # fill with backward fill-
#     dfFillNaWithBackwardFill = replaceNullValue(df, iColumnLabel, "FILL_WITH_BACKWARD_FILL")

# # fill with interpolate-
#     dfFillNaWithInterpolate = replaceNullValue(df, iColumnLabel, "FILL_WITH_INTERPOLATE")


# saved the cleaned files--

# dfDropNa.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_dropna.csv")
# dfFillNaWithMedian.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithMedian.csv")
# dfFillNaWithMode.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithMode.csv")
# dfFillNaWithMean.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithMean.csv")
# dfFillNaWithZero.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithZero.csv")
# dfFillNaWithBackwardFill.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithBackward.csv")
# dfFillNaWithForwardFill.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithForward.csv")
# dfFillNaWithInterpolate.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithInterpolate.c
dfFillNaWithMode.info()
dfFillNaWithMode.info()