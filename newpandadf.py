import pandas as pd
df= {'Name': ['RDJ','SCJ','CH']
    ,'Age' : [50,21,30]
    ,'City' : ['Ny','Boston','CHicago'] }
frame=pd.DataFrame(df)
print(frame[['Name','Age']])
print(frame[(frame['Age']>25) & (frame['City']=='Ny')]) #to give a filter to print only ages greater than 25 nd city Ny
print(frame.groupby('City')['Age'].mean().reset_index) # it gives the avg age of each city 
agg_data = frame.groupby('City').agg({'Age': ['mean’, 'min’, 'max'], 'Name': 'count'}).reset_index()