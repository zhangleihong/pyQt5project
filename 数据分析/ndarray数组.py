"""
@project:数据分析
@author:zlh
@file:ndarray数组.py
@time:2020/4/27 20:53
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

'''
#######            均匀分布
x2 = np.random.uniform(-1,1,1000000)

#1.创建画布
plt.figure(figsize=(20,10),dpi=100)
#2.绘制图像
plt.hist(x2,1000)
#3.显示图像
plt.show()
'''
# 随机生成数组
score = np.random.randint(40,100,(10,5))
print(score)
temp = score[6:,0:5]

print(np.max(temp))

print(np.mean(temp))
# 每列的最大值
print(np.max(temp,axis=0))
# 每行的最大值
print(np.max(temp,axis=1))

# 最大值的下标
print(np.argmax(temp))
print(np.argmax(temp,axis=0))
print(np.argmin(temp,axis=0))
print("---"*20)
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])

print(np.matmul(a,b))

'''
1 2 1 2
3 4 3 4
'''