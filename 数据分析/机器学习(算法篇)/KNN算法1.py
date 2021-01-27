"""
@project:数据分析
@author:zlh
@file:KNN算法1.py
@time:2020/5/3 17:17
"""
from sklearn.neighbors import KNeighborsClassifier
x = [[0],[1],[2],[3]]
y = [0,0,1,1]
# 实例化API
estimator = KNeighborsClassifier(n_neighbors=2)
# 使用fit方法进行训练
estimator.fit(x, y)

res1 = estimator.predict([[1]])
res2 = estimator.predict([[21]])
print(res2)
