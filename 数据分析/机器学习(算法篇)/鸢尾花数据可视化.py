"""
@project:数据分析
@author:zlh
@file:鸢尾花数据可视化.py
@time:2020/5/6 14:28
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# 数据可视化
'''
iris = load_iris()
# 把数据转换成dataframe的格式
iris_d = pd.DataFrame(iris['data'], columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_d['Species'] = iris.target
# print(iris_d)

def plot_iris(iris,col1,col2):
    # hue:目标值 fit_reg:去线条
    sns.lmplot(x=col1,y=col2,data=iris,hue="Species",fit_reg=False)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title('鸢尾花种类分布图')
    plt.show()

plot_iris(iris_d,'Petal_Width','Petal_Length')
'''

# 1、获取鸢尾花数据集
iris = load_iris()
# 对鸢尾花数据集进行分割
# 训练集的特征值x_train 测试集的特征值x_test 训练集的目标值y_train 测试集的目标值y_test
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.2,random_state=22)
print("训练集的特征值是：\n",x_train)
print("训练集的目标值是：\n",y_train)
print("测试集的特征值是：\n",x_test)
print("测试集的目标值是：\n",y_test)
print("x_train:\n", x_train.shape)
# 随机数种子
x_train1, x_test1, y_train1, y_test1 = train_test_split(iris.data, iris.target, random_state=6)
x_train2, x_test2, y_train2, y_test2 = train_test_split(iris.data, iris.target, random_state=6)
print("如果随机数种子不一致：\n", x_train == x_train1)
print("如果随机数种子一致：\n", x_train1 == x_train2)
