import matplotlib.pyplot as plt 
import numpy as np
x=np.arange(-4,5,.1)
y=x*x
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.title('My graph')
plt.plot(x,y,'y-*',linewidth=3, markersize=7)
plt.legend(loc='upper center')
plt.show()