import pandas as pd
wine = pd.read_csv('wine.csv')
# 请注意，数据值全是数值
print(wine.head())
wine = wine.drop('Cultivar', axis = 1)
print(wine.head())

from sklearn.cluster import KMeans
# 创建三个群集
# 随机种子为42
# 可以忽略random_state参数
# 或者使用一个不同的值；使用42可以保证所得结果和本书结果一致
kmeans = KMeans(n_clusters = 3, random_state = 42).fit(wine.values)
# 输出kmeans对象
print(kmeans)
import numpy as np
print(np.unique(kmeans.labels_, return_counts = True))
kmeans_3 = pd.DataFrame(kmeans.labels_, columns = ['cluster'])
print(kmeans_3.head())

from sklearn.decomposition import PCA
# 把数据投射到两个成分上
pca = PCA(n_components = 2).fit(wine)
# 转换数据到新空间
pca_trans = pca.transform(wine)
# 为投影命名
pca_trans_df = pd.DataFrame(pca_trans, columns = ['pca1', 'pca2'])
# 连接数据
kmeans_3 = pd.concat([kmeans_3, pca_trans_df], axis = 1)
print(kmeans_3.head())

import seaborn as sns
import matplotlib.pyplot as plt
fig = sns.lmplot(x = 'pca1', y = 'pca2', data = kmeans_3,
                 hue = 'cluster', fit_reg = False)
plt.show()

wine_all = pd.read_csv('wine.csv')
print(wine_all.head())
pca_all = PCA(n_components = 2).fit(wine_all)
pca_all_trans = pca_all.transform(wine_all)
pca_all_trans_df = pd.DataFrame(pca_all_trans,
                                columns = ['pca_all_1', 'pca_all_2'])
kmeans_3 = pd.concat([kmeans_3,
                      pca_all_trans_df,
                      wine_all['Cultivar']], axis = 1)
# 借助图来比较这些分组
with sns.plotting_context(font_scale = 5):
  fig = sns.lmplot(x = 'pca_all_1',
                   y = 'pca_all_2',
                   data = kmeans_3,
                   row = 'cluster', col = 'Cultivar',
                   fit_reg = False)
plt.show()
# 也可以查看交叉表频率计数
print(pd.crosstab(kmeans_3['cluster'],
                  kmeans_3['Cultivar'],
                  margins = True))
from scipy.cluster import hierarchy
# 再次加载葡萄酒数据集，并删除Cultivar列
wine = pd.read_csv('wine.csv')
wine = wine.drop('Cultivar', axis = 1)
# 层次聚类有许多算法。可以使用matplotlib绘制结果
import matplotlib.pyplot as plt

wine_complete = hierarchy.complete(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_complete)
plt.show()

wine_single = hierarchy.single(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_single)
plt.show()

wine_averge = hierarchy.average(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_averge)
plt.show()

wine_centroid = hierarchy.centroid(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_centroid)
plt.show()

wine_complete = hierarchy.complete(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(
  wine_complete,
  # 默认MATLAB阈值
  color_threshold = 0.7 * max(wine_complete[:, 2]),
  above_threshold_color = 'y'
)
plt.show()