# from sklearn import datasets
# iris = datasets.load_iris()
# data = iris.data
# print(data.shape)
#  (150, 4)
                ############################################################################
import numpy as np
from sklearn import datasets
iris1 = datasets.load_iris(return_X_y=True)
print(iris1)
# return (data,target),Both data and target are list
iris1_X, iris1_y = datasets.load_iris(return_X_y=True)
# means iris1_X = data, iris1_y = target
print(iris1_X)
# data
print(iris1_y)
# target
print("\n")
iris2 = datasets.load_iris(return_X_y=False)
print(iris2)
# return dictionary-like object {'data': array([[5.1, 3.5, 1.4, 0.2],
#        [4.9, 3. , 1.4, 0.2],
#        [4.7, 3.2, 1.3, 0.2],
#        [4.6, 3.1, 1.5, 0.2], 'target': array([0, 0, 0, 0, 0, 0, 0, 0,])}
iris2_X = iris2.data
# note: iris2 is a dict object, put the 'data' carried in the dict for iris2_X
print(iris2_X)

iris2_y = iris2.target
# note: iris2 is a dict object, put the 'target' carried in the dict for iris2_y
print(iris2_y)
