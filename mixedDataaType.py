import pandas as pd

df = pd.DataFrame({
    'mixed': ['abc', 123, 45.6, {'key': 'value'}, [1,2,3]]
})

print(df['mixed'].dtype)                         # Output: object
print(df['mixed'].apply(type))                   # Output: row-wise type
print(df['mixed'].apply(type).value_counts())  