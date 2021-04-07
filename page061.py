import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

'''joint = sns.jointplot(x = "total_bill", y = "tip", data = tips)
joint.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
# 添加标题，设置字号
# 移动轴域上方的文字
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize = 10, y = 1.03)
plt.show()

hexbin = sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
hexbin.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize = 10, y = 1.03)
plt.show()'''
kde, ax = plt.subplots()
ax = sns.kdeplot(data = tips['total_bill'], data2 = tips['tip'], shade = True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_ylabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()
bar, ax = plt.subplots()
ax = sns.barplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Bar plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')
plt.show()

box, ax = plt.subplots()
ax = sns.boxplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Boxplot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()

violin, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()

fig = sns.pairplot(tips)
plt.show()

pair_grid = sns.PairGrid(tips)
# 可以使用plt.scatter代替sns.regplot
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug = True)
plt.show()
