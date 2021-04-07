import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")
# 获取DataFrame每列的数据类型
print(tips.dtypes)
# 把列值转换为字符串使用astype方法
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)
# Series也可以使用astype进行转换
# 转换为字符串
tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.dtypes)
# 转换为float
tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.dtypes)
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print(tips_sub_miss)
print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'], errors = 'ignore'
)
print(tips_sub_miss)
print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'], errors = 'coerce'
)
print(tips_sub_miss)
print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'],
  errors = 'coerce',
  downcast = 'float'
)
print(tips_sub_miss)
print(tips_sub_miss.dtypes)

tips['sex'] = tips['sex'].astype('str')
print(type(tips))
print(tips.info())

tips['sex'] = tips['sex'].astype('category')
print(tips.info())