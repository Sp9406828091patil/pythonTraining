import pandas as pd
# df = pd.read_csv('data.csv')
# print(df)
# # a = 2
# print(df[df['Age'] > 35])
# # print(df['Name'])
# # print(df['Age'])
# df['Age'] = df['Age'] *2
# print(df)

# # print(df.head(5))
# # print(df.tail(5))
# print(df.columns)

# # # print(df.iloc(0, 1)) # call by index
# # print(df.loc(0, 'Age')) # call by label name, here zero is row name not index

# #renaming column
# df.rename(columns = {'name':'Name'}, inplace = True)

# #renaming row index
# df.rename(index = {0 : 'x'}, inplace = True)

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

# #print(df.loc[0:2:2, 'calories'])
# print(df.iloc[0:3:2, 1])
# #print(df.loc[0:2:2, 'calories'])
# print(df.iloc[0, 1])

# print(df.shape)