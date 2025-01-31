import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Create random data for pie chart (5 random categories)
sizes = np.random.randint(1, 10, 5)
labels = ['A', 'B', 'C', 'D', 'E']
colors = plt.cm.viridis(np.linspace(0, 1, len(sizes)))

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title("Random Pie Chart")

# Show plot
plt.show()
