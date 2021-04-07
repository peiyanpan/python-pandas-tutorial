import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
ax = tips['total_bill'].plot.hist()
plt.show()
# 为DataFrame绘制直方图
# 设置alpha通道透明度，使重叠的部分透明可见
fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(alpha = 0.5, bins = 20, ax = ax)
plt.show()

fig ,ax = plt.subplots()
ax = tips['tip'].plot.kde()
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.scatter(x = 'total_bill', y = 'tip', ax = ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = 'total_bill', y = 'tip', ax = ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = 'total_bill', y = 'tip', ax = ax, gridsize = 10)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.box(ax = ax)
plt.show()