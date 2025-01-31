import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('top_output.csv')

# Ensure the '%CPU' column is treated as numeric (in case it's in string format)
df['%CPU'] = pd.to_numeric(df['%CPU'], errors='coerce')

# Group the data by 'USER' and sum the '%CPU' usage for each user
CPU_usage_by_user = df.groupby('USER')['%CPU'].sum().reset_index()

# Sort the result by %CPU usage in descending order
CPU_usage_by_user_sorted = CPU_usage_by_user.sort_values(by='%CPU', ascending=False)

# Print the result
print(CPU_usage_by_user_sorted)

# Calculate total %CPU usage
total_CPU_usage = CPU_usage_by_user_sorted['%CPU'].sum()

# Assume a maximum %CPU usage of 100 (representing full %CPU capacity)
max_CPU_usage = 100

# Calculate unused %CPU
unused_CPU = max_CPU_usage - total_CPU_usage

# Prepare data for pie chart
sizes = list(CPU_usage_by_user_sorted['%CPU']) + [unused_CPU]
labels = list(CPU_usage_by_user_sorted['USER']) + ['Unused %CPU']
colors = plt.cm.viridis(np.linspace(0, 1, len(sizes)))

# Plot pie chart
plt.figure(figsize=(7, 7))
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=140)

# Use a legend for labels to avoid overlap
plt.legend(patches, labels, loc="best", bbox_to_anchor=(1, 0.5))

# Improve appearance of the labels and autotexts
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    
# Add a title
plt.title("%CPU Usage by User and Unused %CPU")

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()

# Optionally, save the result to a new CSV file
CPU_usage_by_user_sorted.to_csv('%CPU_usage_by_user.csv', index=False)
