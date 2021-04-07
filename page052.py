import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'], bins = 10)
axes1.set_title("Histigram of Total Bill")
axes1.set_xlabel("Frequency")
axes1.set_ylabel("Total Bill")
plt.show()

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()

boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot(
  [tips[tips['sex'] == 'Female']['tip'],
   tips[tips['sex'] == 'Male']['tip']],
  labels = ['Famale', 'Male']
)
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')
plt.show()

def recode_sex(sex):
  if sex == 'Female':
    return 0
  else:
    return 1
tips['sex_color'] = tips['sex'].apply(recode_sex)