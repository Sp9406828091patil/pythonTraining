from fetchData.readCsv import readCSV
from fetchData.performEDA import (getNullValueColumns, replaceNullValue)

# get data
filePath = "C:\Users\HP\OneDrive\Documents\pythonTraining\data\weatherstats_toronto_daily.csv"
df = readCSV(filePath)

# get null value columns
nullValueColumns = getNullValueColumns(df)

# get updated 
for iColumnLabel in nullValueColumns:
    dfDropNa = replaceNullValue(df, iColumnLabel, "DROP_NULL_VALUES")

for iColumnLabel in nullValueColumns:
    dfFillNaWithZero = replaceNullValue(df, iColumnLabel, "FILL_WITH_ZERO")