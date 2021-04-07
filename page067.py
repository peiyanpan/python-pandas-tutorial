import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")

violin, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill', hue = 'sex', data = tips, split = True)
plt.show()

scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', fit_reg = False)
plt.show()

fig = sns.pairplot(tips, hue = 'sex')
plt.show()

scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, fit_reg = False, hue = 'sex',
                     scatter_kws = {'s': tips['size'] * 10})
plt.show()

scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips,
                     fit_reg = False, hue = 'sex', markers = ['o', 'x'],
                     scatter_kws = {'s': tips['size'] * 10})
plt.show()

anscombe_plot = sns.lmplot(x = 'x', y = 'y', data = anscombe,
                           fit_reg = False,
                           col = 'dataset', col_wrap = 2)
plt.show()