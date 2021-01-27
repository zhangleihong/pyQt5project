"""
@project:数据分析
@author:zlh
@file:2.1linear_grade.py
@time:2020/5/7 16:04
"""
'''
1.获取数据集
2.数据基本处理（该案例中省略）
3.特征工程（该案例中省略）
4.机器学习
5.模型评估（该案例中省略）
'''
from sklearn.linear_model import LinearRegression
#  平时成绩 期末成绩
x = [[80, 86],
[82, 80],
[85, 78],
[90, 90],
[86, 82],
[82, 90],
[78, 80],
[92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

# 实例化API
estimator = LinearRegression()
# 使用fit方法进行训练
estimator.fit(x,y)

#线性回归系数 estimator.coef_
print("线性回归的系数是：\n",estimator.coef_)

# 打印预测结果
print("输出预测结果:\n",estimator.predict([[100, 80]]))
