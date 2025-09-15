import numpy as np 
import matplotlib.pyplot as plt

#%% 导数趋于零但是本身不一定收敛
t=np.arange(1,6000)
y=np.sin(np.log(t))
yd=np.cos(np.log(t))/t
plt.figure(figsize=(6,3))
plt.plot(t,y,label=r"$f_1(t)$")
plt.plot(t,yd,label=r"$\dot{f}_1(t)$")
plt.grid()
plt.legend()
plt.savefig("../figure/sinlnt.pdf")
plt.show()

#%% 导数趋于零但是本身不一定收敛
t=np.arange(1,6000)
y=np.sqrt(t)*np.sin(np.log(t))
yd=np.sin(np.log(t))/(2*np.sqrt(t))+np.cos(np.log(t))/(np.sqrt(t))
plt.figure(figsize=(6,3))
plt.plot(t,y,label=r"$f_2(t)$")
plt.plot(t,yd,label=r"$\dot{f}_2(t)$")
plt.legend()
plt.grid()
plt.savefig("../figure/sqrttsinlnt.pdf")
plt.show()

#%% 本身收敛但是导数不趋于零
t=np.arange(1,10,0.01)
y=np.exp(-(t))*np.sin(np.exp(2*t))
yd=-np.exp(-(t))*np.sin(np.exp(2*t))+2*np.exp((t))*np.cos(np.exp(2*t))
plt.figure(figsize=(6,3))
plt.plot(t,y,label=r"$f(t)$")
plt.grid()
plt.savefig("../figure/barbalat_f3.pdf")
plt.show()

plt.figure(figsize=(6,3))
plt.plot(t,yd,label=r"$\dot{f}(t)$")
plt.grid()
plt.savefig("../figure/barbalat_f3d.pdf")
plt.show()

#%% 本身收敛但是导数不趋于零
class Yd:
    def __init__(self,T):
        self.T=T
    def __call__(self, t):
        n=(t//self.T)+1
        dt=t%self.T
        if dt<1/(n):
            return 1
        else:
            return 0
t=np.arange(0,10,0.01)
ydf=np.vectorize(Yd(1))
yd=ydf(t)
y=np.zeros_like(t)
for i in range(1,len(t)):
    y[i]=np.trapezoid(yd[:i+1], t[:i+1])

plt.figure(figsize=(6,3))
plt.plot(t,yd,label=r"$\dot{f}(t)$")
plt.grid()
plt.savefig("../figure/barbalat_f4d.pdf")
plt.show()

plt.figure(figsize=(6,3))
plt.plot(t,y,label=r"$\dot{f}(t)$")
plt.grid()
plt.savefig("../figure/barbalat_f4.pdf")
plt.show()

# %%
