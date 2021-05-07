# 导入 pandas 与 numpy 工具包
import pandas as pd
import numpy as np
# 从 sklearn.metrics 里导入 classification_report 模块
from sklearn.metrics import classification_report
# 从 sklearn.preprocessing 里导入 StandardScaler
from sklearn.preprocessing import StandardScaler
# 从 sklearn.linear_model 里导入 LogisticRegression 与 SGDClassifier。
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
# 使用 sklearn.cross_valiation 里的train_test_split 模块用于分割数据。
from sklearn.model_selection import train_test_split

# 创建特征列表
column_names = [
    'Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
    'Uniformity of Cell Shape', 'Marginal Adhesion',
    'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
    'Normal Nucleoli', 'Mitoses', 'Class'
]

# 使用 pandas.read_csv 函数从互联网读取指定数据
data = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
    names=column_names)

# 处理缺失值，将“ ? ”替换为标准缺失值，并丢弃带有缺失值的数据。

# 将 ? 替换为标准缺失值符号表示
data = data.replace(to_replace='?', value=np.nan)
# 丢弃带有缺失值的数据（只要有一个维度有缺失）
data = data.dropna(how='any')

# 查看数据形状。

# 输出 data 的数据量和维度。
data.shape



# 随机采样 25% 的数据用于测试，剩下的 75% 用于构建训练集合。
X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]],
                                                    data[column_names[10]],
                                                    test_size=0.25,
                                                    random_state=33)



# 标准化数据，保证每个维度的特征数据方差为 1 ，均值为 0 。使得预测结果不会被某些维度过大的特征值而主导。
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# 分别使用 Logistic 回归建立模型，代码如下：

# 初始化 LogisticRegression
lr = LogisticRegression()


# 调用 LogisticRegression 中的 fit 函数/模块用来训练模型参数
lr.fit(X_train, y_train)

# 使用训练好的模型 lr 对 X_test 进行预测，结果储存在变量 lr_y_predict 中。
lr_y_predict = lr.predict(X_test)

# 使用逻辑斯蒂回归模型自带的评分函数 score 获得模型在测试集上的准确性结果
print ('Accuracy of LR Classifier:', lr.score(X_test, y_test))
# 利用 classification_report 模块获得 LogisticRegression 其他三个指标的结果
print (classification_report(y_test, lr_y_predict, target_names=['Benign', 'Malignant']))
