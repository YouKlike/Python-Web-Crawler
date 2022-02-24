'''
先假設一個房間寬 5 公尺、長 12 公尺。準備一
台掃地功能壞掉而且會亂跑的掃地機器人,這台
機器人雖然無法掃地但是可以量測地板的骯髒程
度,並用 0 ~ 10 的數值表示(0 為最乾淨,10為
最髒)。放著讓這台機器人在房間裡跑一個晚上,
並在隔天從機器人裡取出數據。而我們預計機器
人會給出這個房間的骯髒程度分佈圖。
'''

import matplotlib.pyplot as plt
import numpy as np
def f(x, y):
    return np.sin(x) ** 5 + np.cos(10 + y*x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z)
plt.show()