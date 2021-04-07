import pandas as pd
housing = pd.read_csv('housing_renamed.csv')
print(housing.head())

import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf

house1 = smf.glm('value_per_sq_ft ~ units + sq_ft + boro',
                 data = housing).fit()
print(house1.summary())

import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax = sns.regplot(x = house1.fittedvalues,
                 y = house1.resid_deviance, fit_reg = False)
plt.show()

res_df = pd.DataFrame({
  'fittedvalues': house1.fittedvalues,
  'resid_deviance': house1.resid_deviance,
  'boro': housing['boro']
})
fig = sns.lmplot(x = 'fittedvalues', y = 'resid_deviance',
                 data = res_df, hue = 'boro', fit_reg = False)
plt.show()

from scipy import stats
resid = house1.resid_deviance.copy()
resid_std = stats.zscore(resid)

fig = statsmodels.graphics.gofplots.qqplot(resid, line = 'r')
plt.show()

fig, ax = plt.subplots()
ax = sns.distplot(resid_std)
plt.show()

# 原始数据包含class列
# 使用class这个词会引发错误，因为class是Python的关键字
# 把列重命名为type
f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'
house1 = smf.ols(f1, data = housing).fit()
house2 = smf.ols(f2, data = housing).fit()
house3 = smf.ols(f3, data = housing).fit()
house4 = smf.ols(f4, data = housing).fit()
house5 = smf.ols(f5, data = housing).fit()
# 针对所有模型，获取系数和相关模型
mod_results = pd.concat([house1.params, house2.params, house3.params,
                         house4.params, house5.params], axis = 1).\
  rename(columns = lambda x: 'house' + str(x + 1)).\
  reset_index().\
  rename(columns = {'index': 'param'}).\
  melt(id_vars = 'param', var_name = 'model', value_name = 'estimate')
print(mod_results.head())
print(mod_results.tail())

fig, ax = plt.subplots()
ax = sns.pointplot(x = "estimate", y = "param", hue = "model",
                   data = mod_results,
                   dodge = True, # jitter the points
                   join = False) # don't connect the points
plt.tight_layout()
plt.show()

model_names = ['house1', 'house2', 'house3', 'house4', 'house5']
house_anova = statsmodels.stats.anova.anova_lm(
  house1, house2, house3, house4, house5
)
house_anova.index = model_names
print(house_anova)

'''house_models = [house1, house2, house3, house4, house5]
house_aic = list(
  map(statsmodels.regression.linear_model.RegressionResults.aic,
      house_models)
)
house_bic = list(
  map(statsmodels.regression.linear_model.RegressionResults.bic,
      house_models)
)
# 字典是无序的
abic = pd.DataFrame({
  'model': model_names,
  'aic': house_aic,
  'bic': house_bic
})
print(abic)'''
def anova_deviance_table(*models):
  return pd.DataFrame({
    'df_residuals': [i.df_resid for i in models],
    'resid_stddev': [i.deviance for i in models],
    'df': [i.df_model for i in models],
    'deviance': [i.deviance for i in models]
  })
f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'

glm1 = smf.glm(f1, data = housing).fit()
glm2 = smf.glm(f2, data = housing).fit()
glm3 = smf.glm(f3, data = housing).fit()
glm4 = smf.glm(f4, data = housing).fit()
glm5 = smf.glm(f5, data = housing).fit()

glm_anova = anova_deviance_table(glm1, glm2, glm3, glm4, glm5)
print(glm_anova)

housing['high_value'] = (housing['value_per_sq_ft'] >= 150).astype(int)
print(housing['high_value'].value_counts())

'''f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'
logistic = statsmodels.genmod.families.family.Binomial(
  link = statsmodels.genmod.families.links.logit
)
glm1 = smf.glm(f1, data = housing, family = logistic).fit()
glm2 = smf.glm(f2, data = housing, family = logistic).fit()
glm3 = smf.glm(f3, data = housing, family = logistic).fit()
glm4 = smf.glm(f4, data = housing, family = logistic).fit()
glm5 = smf.glm(f5, data = housing, family = logistic).fit()
# 显示GLM的偏差
print(anova_deviance_table(glm1, glm2, glm3, glm4, glm5))'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
print(housing.columns)

X_train, X_test, y_train, y_test = train_test_split(
  pd.get_dummies(housing[['units', 'sq_ft', 'boro']],
                 drop_first = True),
  housing['value_per_sq_ft'],
  test_size = 0.20,
  random_state = 42
)
lr = LinearRegression().fit(X_train, y_train)
print(lr.score(X_test, y_test))

from patsy import dmatrices
y, X = dmatrices('value_per_sq_ft ~ units + sq_ft + boro', housing,
                 return_type = "dataframe")
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size = 0.20, random_state = 42
)
lr = LinearRegression().fit(X_train, y_train)
print(lr.score(X_test, y_test))

from sklearn.model_selection import KFold, cross_val_score
# 重新获取住房数据集
housing = pd.read_csv('housing_renamed.csv')

kf = KFold(n_splits = 5)
y, X = dmatrices('value_per_sq_ft ~ units + sq_ft + boro', housing)
# 在每一折上训练并测试数据
coefs = []
scores = []
for train, test in kf.split(X):
  X_train, X_test = X[train], X[test]
  y_train, y_test = y[train], y[test]
  lr = LinearRegression().fit(X_train, y_train)
  coefs.append(pd.DataFrame(lr.coef_))
  scores.append(lr.score(X_test, y_test))
coefs_df = pd.concat(coefs)
coefs_df.columns = X.design_info.column_names
print(coefs_df)

import numpy as np
print(coefs_df.apply(np.mean))

print(scores)

model = LinearRegression()
scores = cross_val_score(model, X, y, cv = 5)
print(scores)

print(scores.mean())
y1, X1 = dmatrices('value_per_sq_ft ~ units + sq_ft + boro',
                   housing)
y2, X2 = dmatrices('value_per_sq_ft ~ units * sq_ft + boro',
                   housing)
y3, X3 = dmatrices('value_per_sq_ft ~ units + sq_ft * boro + type',
                   housing)
y4, X4 = dmatrices('value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type',
                   housing)
y5, X5 = dmatrices('value_per_sq_ft ~ boro + type', housing)
# 拟合模型
model = LinearRegression()

scores1 = cross_val_score(model, X1, y1, cv = 5)
scores2 = cross_val_score(model, X2, y2, cv = 5)
scores3 = cross_val_score(model, X3, y3, cv = 5)
scores4 = cross_val_score(model, X4, y4, cv = 5)
scores5 = cross_val_score(model, X5, y5, cv = 5)
# 查看交叉验证分数
score_df = pd.DataFrame([scores1, scores2, scores3,
                         scores4, scores5])
print(score_df.apply(np.mean, axis = 1))