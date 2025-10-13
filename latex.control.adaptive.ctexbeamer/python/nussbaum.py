from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def rhs(t,states,params):
    x=states[0]
    z=states[1]
    
    u=params['N'](z)*x
    dxdt=params['g']*u

    dzdt=x**2
    return [dxdt,dzdt]

def simulate(params):
    t_span=[0,params['t_max']]
    y0=params['y0']
    sol=solve_ivp(rhs,t_span,y0,args=(params,),max_step=params['dt'],method='RK45')
    return sol

params={}
params['N']=lambda z:np.sin(3*np.pi*z)*np.exp(0.01*z**2)
params['g']=1
params['dt']=0.01

params['t_max']=100
params['y0']=[1,1]
sol=simulate(params)

x=np.linspace(0,1,100)
n=params['N'](x)

plt.figure()
plt.plot(sol.t,sol.y[0,:],label='x(t)')
plt.plot(sol.t,sol.y[1,:],label='z(t)')
plt.grid()
plt.legend()

plt.show()