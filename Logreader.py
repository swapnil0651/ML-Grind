import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('top_output.csv')

# Ensure the 'CPU' column is treated as numeric (in case it's in string format)
df['CPU'] = pd.to_numeric(df['CPU'], errors='coerce')

# Group the data by 'USER' and sum the 'CPU' usage for each user
cpu_usage_by_user = df.groupby('USER')['CPU'].sum().reset_index()

# Sort the result by CPU usage in descending order
cpu_usage_by_user_sorted = cpu_usage_by_user.sort_values(by='CPU', ascending=False)

# Print the result
print(cpu_usage_by_user_sorted)

# Optionally, save the result to a new CSV file
cpu_usage_by_user_sorted.to_csv('cpu_usage_by_user.csv', index=False)
