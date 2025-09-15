import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import matplotlib.gridspec as gridspec

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 创建一个图形，用于展示所有结果
plt.figure(figsize=(15, 18))
gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1])

# ---------------------- 1. 矩形脉冲函数及其积分 ----------------------
def rectangle_pulse(x, n):
    """定义矩形脉冲函数"""
    return n * ((x >= 0) & (x <= 1/n**2)).astype(float)

def rectangle_pulse_integral(x, n):
    """计算矩形脉冲函数的积分"""
    res = np.zeros_like(x)
    for i, val in enumerate(x):
        if val <= 0:
            res[i] = 0
        elif val <= 1/n**2:
            res[i] = n * val
        else:
            res[i] = 1/n  # 积分上限超过脉冲宽度时的结果
    return res

# 生成x值
x1 = np.linspace(0, 0.1, 1000)

# 绘制矩形脉冲函数
ax1 = plt.subplot(gs[0, 0])
for n in [5, 10, 20]:
    ax1.plot(x1, rectangle_pulse(x1, n), label=f'n={n}')
ax1.set_title('(1) 矩形脉冲函数 f_n(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('f_n(x)')
ax1.grid(True)
ax1.legend()

# 绘制矩形脉冲函数的积分
ax2 = plt.subplot(gs[0, 1])
for n in [5, 10, 20]:
    ax2.plot(x1, rectangle_pulse_integral(x1, n), label=f'n={n}')
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.3)
ax2.set_title('(1) 矩形脉冲函数的积分')
ax2.set_xlabel('x')
ax2.set_ylabel('∫f_n(t)dt')
ax2.grid(True)
ax2.legend()

# ---------------------- 2. 高频震荡函数及其积分 ----------------------
def oscillating_function(x, n):
    """定义高频震荡函数"""
    return np.sqrt(n) * np.sin(n * x)

def oscillating_integral(x, n):
    """计算高频震荡函数的积分"""
    return (1 - np.cos(n * x)) / np.sqrt(n)

# 生成x值
x2 = np.linspace(0, 1, 10000)  # 使用更多点以捕捉高频震荡

# 绘制高频震荡函数
ax3 = plt.subplot(gs[1, 0])
for n in [10, 50, 100]:
    ax3.plot(x2, oscillating_function(x2, n), label=f'n={n}', alpha=0.7)
ax3.set_title('(2) 高频震荡函数 √n·sin(nx)')
ax3.set_xlabel('x')
ax3.set_ylabel('f_n(x)')
ax3.grid(True)
ax3.legend()

# 绘制高频震荡函数的积分
ax4 = plt.subplot(gs[1, 1])
for n in [10, 50, 100]:
    ax4.plot(x2, oscillating_integral(x2, n), label=f'n={n}')
ax4.axhline(y=0, color='r', linestyle='--', alpha=0.3)
ax4.set_title('(2) 高频震荡函数的积分')
ax4.set_xlabel('x')
ax4.set_ylabel('∫f_n(t)dt')
ax4.grid(True)
ax4.legend()

# ---------------------- 3. 傅里叶积分型函数及其积分 ----------------------
def fourier_function(x):
    """定义傅里叶积分型函数 sin(x²)"""
    return np.sin(x**2)

def fourier_integral(x):
    """计算傅里叶积分型函数的局部积分"""
    res = np.zeros_like(x)
    for i, val in enumerate(x):
        # 计算从val到val+1的积分
        integral, _ = integrate.quad(fourier_function, val, val + 1)
        res[i] = integral
    return res

# 生成x值（较大范围以展示震荡特性）
x3 = np.linspace(1, 30, 1000)

# 绘制傅里叶积分型函数
ax5 = plt.subplot(gs[2, 0])
ax5.plot(x3, fourier_function(x3))
ax5.set_title('(3) 傅里叶积分型函数 sin(x²)')
ax5.set_xlabel('x')
ax5.set_ylabel('f(x)')
ax5.grid(True)

# 绘制傅里叶积分型函数的局部积分
ax6 = plt.subplot(gs[2, 1])
ax6.plot(x3, fourier_integral(x3))
ax6.axhline(y=0, color='r', linestyle='--', alpha=0.3)
ax6.set_title('(3) sin(x²)的局部积分 ∫[x,x+1] sin(t²)dt')
ax6.set_xlabel('x')
ax6.set_ylabel('积分值')
ax6.grid(True)

# 调整布局并显示图形
plt.tight_layout()
plt.show()
