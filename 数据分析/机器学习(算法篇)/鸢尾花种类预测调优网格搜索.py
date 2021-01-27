"""
@project:数据分析
@author:zlh
@file:鸢尾花种类预测调优网格搜索.py
@time:2020/5/7 14:13
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
'''
1.获取数据集
2.数据基本处理
3.特征工程
4.机器学习(模型训练)
5.模型评估
'''
# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
# 3、特征工程：特征值的标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4、机器学习(模型训练)
# 4.1实例化一个估计器
estimator = KNeighborsClassifier()
# 4.2模型调优 交叉验证 ，网格搜索
param_grid = {"n_neighbors":[1,3,5,7]}
'''
estimator：估计器对象
param_grid：估计器参数(dict){“n_neighbors”:[1,3,5]}
cv：指定几折交叉验证
'''
estimator = GridSearchCV(estimator,param_grid=param_grid,cv=5)
# 4.3模型训练
estimator.fit(x_train, y_train)
# 5、模型评估
# 方法1：比对真实值和预测值
y_predict = estimator.predict(x_test)
print("预测结果为:\n", y_predict)
print("比对真实值和预测值：\n", y_predict == y_test)
# 方法2：直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)

# 方法三：查看调优后属性
'''
bestscore__:在交叉验证中验证的最好结果
bestestimator：最好的参数模型
cvresults:每次交叉验证后的验证集准确率结果和训练集准确率结果
'''
print("在交叉验证中验证的最好结果：\n", estimator.best_score_)
print("最好的参数模型：\n", estimator.best_estimator_)
print("每次交叉验证后的准确率结果：\n", estimator.cv_results_)