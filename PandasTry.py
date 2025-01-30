import pandas as pd
# its use to make data presentable
#to make sense of the data
# to assign framings to the tabular data
#helps in data framing
# deleting null, garbage, duplicate data
# can be used Like SQL
#create merges, joins, gorup_OPs, handle missing data
# it provides time series functionality
# it tags the logs with timestamp
df= {'Name': ['RDJ','SCJ','CH']
    ,'Age' : [50,21,30]
    ,'City' : ['Ny','Boston','CHicago'] }  #this is like dictionary
print (df)
frame=pd.DataFrame(df) #this is a dataframe
print(frame)
print(type(frame))
print(frame.shape) #it will come 3 by 3 because it doesnt show frames
print(frame.columns) # to see the frames

print(frame.dtypes) #to get the dtatatypes
frame.to_csv('people.csv', index=False) #to create a csv file