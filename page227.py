import pandas as pd
acs = pd.read_csv('acs_ny.csv')
print(acs.columns)
print(acs.head())

acs['ge150k'] = pd.cut(acs['FamilyIncome'],
                       [0, 150000, acs['FamilyIncome'].max()],
                       labels = [0, 1])
acs['ge150k_i'] = acs['ge150k'].astype(int)
print(acs['ge150k_i'].value_counts())
print(acs.info())

import statsmodels.formula.api as smf
model = smf.logit('ge150k_i ~ HouseCosts + NumWorkers + '\
                  'OwnRent + NumBedrooms + FamilyType',
                  data = acs)
results = model.fit()
print(results.summary())

import numpy as np
odds_ratios = np.exp(results.params)
print(odds_ratios)

print(acs.OwnRent.unique())

predictors = pd.get_dummies(
  acs[['HouseCosts', 'NumWorkers', 'OwnRent', 'NumBedrooms',
       'FamilyType']],
  drop_first = True
)
# 使用linear_model模块的LogisticRegression对象

from sklearn import linear_model
lr = linear_model.LogisticRegression(max_iter=1000)
# 调用fit方法拟合模型，这和拟合线性模型的方法相同
results = lr.fit(X = predictors, y = acs['ge150k_i'])
# 输出系数
print(results.coef_)
print(results.intercept_)
values = np.append(results.intercept_, results.coef_)
# 得到值的名称
names = np.append('intercept', predictors.columns)
# 全部放入一个带标签的DataFrame中
results = pd.DataFrame(values, index = names,
                       columns = ['coef'])
print(results)
results['or'] = np.exp(results['coef'])
print(results)
results = smf.poisson(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs
).fit()
print(results.summary())

import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
model = smf.glm(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs,
  family = sm.families.Poisson(sm.genmod.families.links.log)
)
results = model.fit()
print(results.summary())

model = smf.glm(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs,
  family = sm.families.NegativeBinomial(sm.genmod.families.links.log)
)
results = model.fit()
print(results.summary())

bladder = pd.read_csv('bladder.csv')
print(bladder.head())
print(bladder['rx'].value_counts())

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(bladder['stop'], event_observed = bladder['event'])
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax = kmf.survival_function_.plot(ax = ax)
ax.set_title('Survival function')
plt.show()

fig, ax = plt.subplots()
ax = kmf.plot(ax = ax)
ax.set_title('Survival with confidence intervals')
plt.show()

from lifelines import CoxPHFitter
cph = CoxPHFitter()
# 传入用作自变量的列
cph_bladder_df = bladder[['rx', 'number', 'size',
                          'enum', 'stop', 'event']]
cph.fit(cph_bladder_df, duration_col = 'stop', event_col = 'event')
# 输出系数
print(cph.print_summary())

rx1 = bladder.loc[bladder['rx'] == 1]
rx2 = bladder.loc[bladder['rx'] == 2]
kmf1 = KaplanMeierFitter()
kmf1.fit(rx1['stop'], event_observed = rx1['event'])

kmf2 = KaplanMeierFitter()
kmf2.fit(rx2['stop'], event_observed = rx2['event'])

fig, axes = plt.subplots()
kmf1.plot_loglogs(ax = axes)
kmf2.plot_loglogs(ax = axes)

axes.legend(['rx1', 'rx2'])
plt.show()

cph_start = CoxPHFitter()
cph_start.fit(cph_bladder_df, duration_col = 'stop', event_col = 'event',
              strata = ['rx'])
print(cph_start.print_summary())
