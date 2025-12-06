import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from pathlib import Path
output=Path(__file__).parent.joinpath("out")

# ===================== 1. 定义系统参数 =====================
delta = 0.03    # 阻尼系数
alpha = -1      # 线性项系数
beta = 1        # 立方项系数
gamma = 0.8     # 扰动幅值
omega = 0.2     # 扰动频率
phi = 0.1       # 扰动相位
rho1 = 1.0      # 状态变换参数
rho2 = 1.0      # 控制器增益
Lambda = np.diag([1.0, 1.0, 1.0, 1.0, 1.0])  # 自适应律增益矩阵

# 扰动分解为gamma1*cos(ωt) + gamma2*sin(ωt)
gamma1 = gamma * np.cos(phi)
gamma2 = gamma * np.sin(phi)

# 真实参数向量 μ (用于对比，仿真中自适应律不需要已知)
mu_true = np.array([-delta + rho1, -alpha, -beta, gamma1, gamma2])

# ===================== 2. 定义系统动力学 =====================
def duffing_adaptive(t, state):
    """
    状态向量: [x1, x2, hat_mu0, hat_mu1, hat_mu2, hat_mu3, hat_mu4]
    - x1, x2: 系统状态
    - hat_mu0~4: 自适应参数估计值 (对应μ的5个元素)
    """
    x1, x2 = state[0], state[1]
    hat_mu = state[2:7]  # 自适应参数估计

    # 1. 状态变换 X2 = x2 + rho1*x1
    X2 = x2 + rho1 * x1

    # 2. 构造f0向量
    cos_wt = np.cos(omega * t)
    sin_wt = np.sin(omega * t)
    f0 = np.array([x2, x1, x1**3, cos_wt, sin_wt])

    # 3. 控制器 u (公式5.55)
    u = -rho2 * X2 - np.dot(f0.T, hat_mu)

    # 4. 系统状态导数
    dx1_dt = x2
    dx2_dt = -delta*x2 - alpha*x1 - beta*x1**3 + gamma1*cos_wt + gamma2*sin_wt + u

    # 5. 自适应律: d(hat_mu)/dt = Λ * X2 * f0
    d_hat_mu_dt = Lambda @ (X2 * f0)

    # 组装所有状态导数
    d_state_dt = np.hstack([dx1_dt, dx2_dt, d_hat_mu_dt])
    return d_state_dt

# ===================== 3. 仿真配置 =====================
t_span = (0, 100)    # 仿真时间范围
t_eval = np.linspace(0, 100, 1000)  # 时间采样点
x0 = [1.0, 0.5]      # 系统初始状态 [x1(0), x2(0)]
hat_mu0 = [0.0]*5    # 自适应参数初始估计 (全零)
initial_state = x0 + hat_mu0  # 完整初始状态

# ===================== 4. 数值求解微分方程 =====================
sol = solve_ivp(
    fun=duffing_adaptive,
    t_span=t_span,
    y0=initial_state,
    t_eval=t_eval,
    method='RK45',  # 龙格-库塔法
    rtol=1e-6,      # 相对误差
    atol=1e-9       # 绝对误差
)

# 提取仿真结果
t = sol.t
x1 = sol.y[0]
x2 = sol.y[1]
hat_mu = sol.y[2:7]  # 自适应参数估计轨迹

# 重新计算控制信号u (用于绘图)
X2 = x2 + rho1 * x1
f0 = np.vstack([x2, x1, x1**3, np.cos(omega*t), np.sin(omega*t)]).T
u = -rho2 * X2 - np.sum(hat_mu.T * f0, axis=1)

# ===================== 5. 绘图 =====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['axes.unicode_minus'] = False    # 负号显示
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 4), sharex=True)

# 子图1: x1(t) 轨迹
ax1.plot(t, x1, 'b-', linewidth=1.5, label='$x_1(t)$')
ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax1.set_ylabel('$x_1$')
ax1.set_title('Duffing方程自适应镇定仿真结果')
ax1.legend()
ax1.grid(alpha=0.3)

# 子图2: x2(t) 轨迹
ax2.plot(t, x2, 'g-', linewidth=1.5, label='$x_2(t)$')
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax2.set_ylabel('$x_2$')
ax2.legend()
ax2.grid(alpha=0.3)

# 子图3: 控制信号u(t)
ax3.plot(t, u, 'r-', linewidth=1.5, label='$u(t)$')
ax3.set_xlabel('时间 $t$ (s)')
ax3.set_ylabel('控制信号 $u$')
ax3.legend()
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(output.joinpath("duffing-x.pdf"))

# 额外: 绘制自适应参数估计收敛曲线
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4), sharex=True)
mu_labels = [r'$\hat{\mu}_0$', r'$\hat{\mu}_1$', r'$\hat{\mu}_2$', r'$\hat{\mu}_3$', r'$\hat{\mu}_4$']
axs=[ax1,ax1,ax2,ax2,ax2]
for i in range(5):
    ax=axs[i]
    p=ax.plot(t, hat_mu[i], '-', linewidth=1.5, label=mu_labels[i])
    ax.axhline(y=mu_true[i], color=p[0].get_color(), linestyle='--') #, label=f'真实值: {mu_true[i]:.2f}'
    # axs[i].set_ylabel(mu_labels[i])
    # axs[i].legend(ncol=2)
    ax.grid(alpha=0.3)
ax1.legend(ncol=2)
ax2.legend(ncol=3)
plt.xlabel('时间 $t$ (s)')
plt.suptitle('自适应参数估计收敛轨迹')
plt.tight_layout()
plt.savefig(output.joinpath("duffing-mu.pdf"))
plt.pause(10)