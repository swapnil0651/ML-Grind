import pandas as pd
df=pd.read_csv('people.csv')
print(df.head()) #only shows 5 values to check the type
df.to_csv('new-data.csv', index=False)
