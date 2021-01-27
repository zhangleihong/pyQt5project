"""
@project:数据分析
@author:zlh
@file:pandasDemo.py
@time:2020/5/1 0:10
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
score = np.random.randint(40,100,(10,5))
print(score)
score_df = pd.DataFrame(score)
print(score_df)
# 加名称
subjects = ['语文','数学','英语','政治','体育']
stu = ["同学" + str(i) for i in range(score_df.shape[0])]
data = pd.DataFrame(score,columns=subjects,index=stu)
print(data)
# 重设索引
data.index = stu
data.reset_index()
print(data.reset_index())
print(data.reset_index(drop=True))


data = data.drop(["city_confirmedCount","city_suspectedCount","city_curedCount","city_deadCount","updateTime"],axis=1)