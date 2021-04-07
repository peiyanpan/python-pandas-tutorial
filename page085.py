import pandas as pd

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
# 获取第四行
print(row_concat.iloc[3,])
# 新建一行数据
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)
# 尝试向DataFrame添加新行
print(pd.concat([df1, new_row_series]))
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']],
                          columns = ['A', 'B', 'C', 'D'])
print(new_row_df)
print(pd.concat([df1, new_row_df]))
print(df1.append(df2))
print(df1.append(new_row_df))
data_dict = {'A': 'n1',
             'B': 'n2',
             'C': 'n3',
             'D': 'n4'}
print(df1.append(data_dict, ignore_index = True))

row_concat_i = pd.concat([df1, df2, df3],ignore_index = True)
print(row_concat_i)
col_concat = pd.concat([df1, df2, df3], axis = 1)
print(col_concat)
print(col_concat['A'])
# 添加一列
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)

col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)

print(pd.concat([df1, df2, df3], axis = 1, ignore_index = True))

# 调整DataFrame
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']
print(df1)
print(df2)
print(df3)
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
print(pd.concat([df1, df2, df3], join = 'inner'))
print(pd.concat([df1, df3], ignore_index = False, join = 'inner'))

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]
print(df1)
print(df2)
print(df3)
# 按列连接
col_concat = pd.concat([df1, df2, df3], axis = 1)
print(col_concat)
print(pd.concat([df1, df3], axis = 1, join = 'inner'))