import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x=np.random.randn(100)
y=np.random.randn(100)
colors=np.random.randn(100)
plt.figure(figsize=(8,6))
plt.scatter(x,y,c=colors,alpha=0.8,cmap='viridis')
plt.colorbar(label='Color Intensity')
plt.title("practice scatter")
plt.show()