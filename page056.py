import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
# 使用subplot函数创建画布，并在其中添加各个子图
hist, ax = plt.subplots()

# 使用seaborn的distplot函数绘图
ax = sns.distplot(tips['total_bill'], kde = False)
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()

den, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], hist = False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
plt.show()

hist_den_rug, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'],rug = True)
ax.set_title('Total Bill Histogram with Density and Rug Plot')
ax.set_xlabel('Total Bill')
plt.show()

count, ax = plt.subplots()
ax = sns.countplot('day', data = tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
plt.show()

scatter, ax = plt.subplots()
ax = sns.regplot(x = 'total_bill', y = 'tip', data = tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()

fig = sns.lmplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()

joint = sns.jointplot(x = 'total_bill', y = 'tip', data = tips)
joint.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
# 添加标题，设置字号
# 移动轴域上方的文字
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize = 10, y = 1.03)
