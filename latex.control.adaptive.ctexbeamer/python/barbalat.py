import numpy as np 
import matplotlib.pyplot as plt

x=np.arrange(1,100)
y=1/x-np.sin(x)/x/x
plt.figure()
plt.plot(x,y)
