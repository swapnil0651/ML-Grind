import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

  # or 'Qt5Agg', or 'WebAgg'

x = [1,2,3,4,5]
y = [2,4,9,5,12]
#plt.figure(figsize=(8,4))
#plt.plot(x,y)
plt.plot(x,y,marker = 'o', linestyle= '-',color ='b' ,label ='Line Plot')
#plt.show()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.legend()
plt.show()
