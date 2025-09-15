#%%
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#%%
def w1(t):
    return np.sin(t)

def rhs(t,x,w_func):
    e=x[0]
    theta=x[1]
    w=w_func(t)
    de=-e+theta*w
    dtheta=-e*w
    return np.array([de,dtheta])

t_eval=np.arange(0,40,0.01)
sol=solve_ivp(rhs,[0,40],[-1,1.4],args=(w1,),dense_output=True,t_eval=t_eval)
plt.figure(figsize=(6,3))
plt.plot(sol.t,sol.y[0,:],label=r"$e$")
plt.plot(sol.t,sol.y[1,:],"--",label=r"$\theta$")
plt.plot(sol.t,np.vectorize(w1)(sol.t),"--",label=r"$w(t)$")
plt.legend()
plt.grid()
plt.savefig("../figure/simple-pe.pdf")
plt.show()


# %%
def w2(t):
    if t<2*np.pi:
        w=np.sin(t)
    else:
        w=0
    return w


t_eval=np.arange(0,40,0.01)
sol=solve_ivp(rhs,[0,40],[-1,1.4],args=(w2,),dense_output=True,t_eval=t_eval)
plt.figure(figsize=(6,3))
plt.plot(sol.t,sol.y[0,:],label=r"$e$")
plt.plot(sol.t,sol.y[1,:],label=r"$\theta$")
plt.plot(sol.t,np.vectorize(w2)(sol.t),"--",label=r"$w(t)$")
plt.legend()
plt.grid()
plt.savefig("../figure/simple-npe.pdf")
plt.show()
# %%
