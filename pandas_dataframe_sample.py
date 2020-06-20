# %%
import pandas as pd

df = pd.read_csv('/Users/mac_root/Documents/workspace/Files/Workspace/titanic/train.csv', index_col=0, header=0)
df_two = df.copy()
df_three = df.copy()

print(df.columns.values)
print('------------------------------------------')
print(df.index.values)

# %%

#特定列を取得する方法
print(df[['Survived']].head(3))
print(type(df[['Survived']]))
#下記指定も可能　※予約語とかぶるとそちらが優先されてエラーになる可能性がある
print(df.Survived.head(3))
print(type(df.Survived))

# %%

# 個別の値を参照する方法[index,column]
print(df.at[15, 'Age'])
print(df.at[15, 'Survived'])

# %%
