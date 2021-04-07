import pandas as pd 
import matplotlib.pyplot as plt
# read_csv:加载csv数据文件
# 把sep参数设置成\t,显示指明使用制表符分隔
df = pd.read_csv('gapminder.tsv',sep='\t') 
# 调用head方法,只显示前五行数据
print(df.head())
'''
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
'''
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
# shape属性指明DataFrame的行数和列数
print(df.shape) # (1704, 6)
# 获取列名
print(df.columns) # Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')
# 获取每列的dtype
print(df.dtypes)
'''
country       object
continent     object
year           int64
lifeExp      float64
pop            int64
gdpPercap    float64
dtype: object
'''
# 获取更多数据信息
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1704 entries, 0 to 1703
Data columns (total 6 columns):
country      1704 non-null object
continent    1704 non-null object
year         1704 non-null int64
lifeExp      1704 non-null float64
pop          1704 non-null int64
gdpPercap    1704 non-null float64
dtypes: float64(2), int64(2), object(2)
memory usage: 80.0+ KB
None
'''
# 只获取country列,并将其保存到一个变量中
country_df = df['country']
# 显示前五行
print(country_df.head())
# 显示最后五行
print(country_df.tail())
# 查看country,continent,year列
subset = df[['country','continent','year']]
print(subset.head())
print(subset.tail())

print(df.loc[0])

print(df.loc[99])

number_of_rows = df.shape[0]
last_row_Index = number_of_rows - 1
print(df.loc[last_row_Index])

print(df.tail(n=1))

print(df.loc[[0,99,999]])

print(df.iloc[1])

print(df.iloc[99])

print(df.iloc[-1])

print(df.iloc[[0,99,999]])

subset = df.loc[:,['year','pop']]
print(subset.head())

subset = df.iloc[:,[2,4,-1]]
print(subset.head())

small_range = list(range(5)) # [0,1,2,3,4]
subset = df.iloc[:,small_range]
print(subset.head())

small_range = list(range(3,6)) # [3,4,5]
subset = df.iloc[:,small_range]
print(subset.head())

small_range = list(range(0,6,2)) # [0,2,4] 获取0-6之间的偶数，不包含6
subset = df.iloc[:,small_range]
print(subset.head())

subset = df.iloc[:,:3]
print(subset.head())

subset = df.iloc[:,3:6]
print(subset.head())

subset = df.iloc[:,0:6:2] # 获取3-5列
print(subset.head())

print(df.loc[42,'country'])

print(df.iloc[[0,99,999],[0,3,5]])

print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])

print(df.head(n=10))

print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp)

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

multi_group_var = df.\
       groupby(['year','continent'])\
       [['lifeExp','gdpPercap']].\
       mean()
print(multi_group_var)

flat = multi_group_var.reset_index()
print(flat.head(15))

print(df.groupby('continent')['country'].nunique())

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()