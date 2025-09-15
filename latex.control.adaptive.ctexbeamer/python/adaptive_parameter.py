from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#%%
def rhs(t,x):
    e=x[0]
    theta=x[1]
    w=np.sin(t)
    de=-e+theta*w
    dtheta=-e*w
    return np.array([de,dtheta])

sol=solve_ivp(rhs,[0,40],[-1,0.4])
plt.figure(figsize=(6,3))
plt.plot(sol.t,sol.y[0,:],label=r"$e$")
plt.plot(sol.t,sol.y[1,:],label=r"$\theta$")
plt.legend()
plt.grid()
plt.savefig("../figure/simple-pe.pdf")
plt.show()
# %%
def rhs(t,x):
    e=x[0]
    theta=x[1]
    if t<5:
        w=1
    else:
        w=0
    de=-e+theta*w
    dtheta=-e*w
    return np.array([de,dtheta])

sol=solve_ivp(rhs,[0,40],[-1,0.4])
plt.figure(figsize=(6,3))
plt.plot(sol.t,sol.y[0,:],label=r"$e$")
plt.plot(sol.t,sol.y[1,:],label=r"$\theta$")
plt.legend()
plt.grid()
plt.savefig("../figure/simple-npe.pdf")
plt.show()
# %%
