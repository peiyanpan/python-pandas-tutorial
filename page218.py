import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())

import statsmodels.formula.api as smf
model = smf.ols(formula = 'tip ~ total_bill', data = tips)
results = model.fit()
print(results.summary())
print(results.params)
print(results.conf_int())
from sklearn import linear_model

lr = linear_model.LinearRegression()
'''predicted = lr.fit(X = tips['total_bill'],
                   y = tips['tip'])'''
# 请注意，X是大写，y是小写
# 重塑数据，使其符合sklearn的要求
predicted = lr.fit(X = tips['total_bill'].values.reshape(-1, 1),
                   y = tips['tip'])

print(predicted.coef_)
print(predicted.intercept_)

model = smf.ols(formula = 'tip ~ total_bill + size', data = tips).fit()
print(model.summary())

print(tips.info())

print(tips.sex.unique())

model = smf.ols(
  formula = 'tip ~ total_bill + size + sex + smoker + day + time',
  data = tips
).\
  fit()
print(model.summary())

print(tips.day.unique())

lr = linear_model.LinearRegression()
# 由于执行的是多元回归，所以无需重塑X值
predicted = lr.fit(X = tips[['total_bill', 'size']],
                   y = tips['tip'])
print(predicted.coef_)
print(predicted.intercept_)

tips_dummy = pd.get_dummies(
  tips[['total_bill', 'size',
        'sex', 'smoker', 'day', 'time']]
)
print(tips_dummy.head())
x_tips_dummy_ref = pd.get_dummies(
  tips[['total_bill', 'size',
        'sex', 'smoker', 'day', 'time']], drop_first = True
)
print(x_tips_dummy_ref.head())
# 拟合模型
lr = linear_model.LinearRegression()
predicted = lr.fit(X = x_tips_dummy_ref,
                   y = tips['tip'])
print(predicted.coef_)
print(predicted.intercept_)

import numpy as np
# 创建模型并拟合
lr = linear_model.LinearRegression()
predicted = lr.fit(X = x_tips_dummy_ref, y = tips['tip'])
# 获取截距以及其他系数
values = np.append(predicted.intercept_, predicted.coef_)
# 获取值的名称
names = np.append('intercept', x_tips_dummy_ref.columns)
# 把所有项放入一个带标签的DataFrame中
results = pd.DataFrame(values, index = names,
                       columns = ['coef'] # 这里用方括号
                       )
print(results)