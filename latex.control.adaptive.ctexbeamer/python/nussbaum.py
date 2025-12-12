from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
output=Path(__file__).parent.joinpath("out")

def rhs(t,states,params):
    x=states[0]
    z=states[1]
    
    u=params['N'](z)*x
    delta=params.get("delta",0)
    dxdt=params['g']*u+delta

    dzdt=x**2
    return [dxdt,dzdt]

def simulate(params):
    t_span=[0,params['t_max']]
    y0=params['y0']
    sol=solve_ivp(rhs,t_span,y0,args=(params,),max_step=params['dt'],method='RK45')
    return sol

def plt_show():
    pass

def plot(params,sol,fileprefix=""):
    #%%
    plt.figure(figsize=(6,2))
    plt.plot(sol.t,sol.y[0,:],label='x(t)')
    plt.grid()
    plt.legend()
    plt.xlim([0,40])
    plt.savefig(output.joinpath(fileprefix+"_x.pdf"))
    plt.figure(figsize=(6,2))
    plt.plot(sol.t,sol.y[1,:],label='z(t)')
    plt.grid()
    plt.legend()
    plt.xlim([0,40])
    plt.savefig(output.joinpath(fileprefix+"_z.pdf"))
    plt_show()
    plt.figure(figsize=(6,2))
    n2=np.array([params['N'](xi) for xi in sol.y[1,:]])
    plt.plot(sol.t,n2,label='N(z(t))')
    plt.grid()
    plt.xlim([0,40])
    plt.legend()
    plt.savefig(output.joinpath(fileprefix+"_n.pdf"))
    plt_show()
    plt.figure(figsize=(6,2))
    u2=np.array([params['N'](xi)*xi for xi in sol.y[1,:]])
    plt.plot(sol.t,u2,label='u(t)')
    plt.grid()
    plt.xlim([0,40])
    plt.legend()
    plt.savefig(output.joinpath(fileprefix+"_u.pdf"))
    plt_show()

params={}
params['N']=lambda z:np.sin(3*np.pi*z)*np.exp(0.01*z**2)
params['g']=1
params['dt']=0.01

params['t_max']=100
params['y0']=[1,1]


#%%
x=np.arange(0,16,0.01)
n=np.array([params['N'](xi) for xi in x])
plt.figure(figsize=(6,3))
plt.plot(x,n)
plt.grid(True)
plt.xlabel("$s$")
plt.ylabel("$v$")
plt.savefig(output.joinpath("nussbaum.pdf"))


#%%
sol=simulate(params)
plot(params,sol,fileprefix="n1")

#%%
params2=params.copy()
params2["g"]=-1
sol2=simulate(params2)
plot(params2,sol2,fileprefix="n2")
#%%
params2=params.copy()
params2["delta"]=1
sol2=simulate(params2)
plot(params2,sol2,fileprefix="n3delta")