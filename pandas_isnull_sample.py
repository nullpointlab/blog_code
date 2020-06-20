# %%
import pandas as pd

df = pd.read_csv('/Users/mac_root/Documents/workspace/Files/Workspace/titanic/train.csv')
df_two = df.copy()
df_three = df.copy()

df.info()
print('------------------------------------------')
df_two.info()
print('------------------------------------------')
df_three.info()

# %%

# 欠損値確認　True:欠損　False:データあり
df.isnull()

# %%
# 欠損値の集計　カラムごとに集計
df.isnull().sum()


# %%
# 欠損値、データ型の要約
df.info()

# %%

#########################################
# dropna関数の説明
# 基本的には返り値が変更されるだけで、実際のデータでは削除はされない
#########################################

# 欠損している行、列を削除する
df.dropna().shape

# %%

# 欠損している列や行の削除指定
# 引数 axis 0('columns'):行削除　1('rows')):列削除
# 引数 how 'all':axisで指定した列or行が全てNaNであれば削除
# 'any':axisで指定した列or行が1つでもNaNであれば削除
df.dropna(axis='columns').shape

# %%

# 非欠損値が〇〇個存在する場合は削除しない
df.dropna(thresh=11).shape

# %%

# inplace=Trueでデータ元に反映させることが可能
df_two.dropna(thresh=11).isnull().sum()
df_two.dropna(inplace=True)

df.info()
print('------------------------------------------')
df_two.info()


# %%
#########################################
# fillna欠損値を埋める方法
#########################################

# 数値で埋める方法
df.fillna(0).head()

# %%

# 文字列で埋める方法
df.fillna('missing')

# %%

# 列ごとに埋める方法
df.fillna({'Age':0, 'Cabin': 'Z00'})

# %%

# 直前の値で埋める方法(forward fillの略)
df.fillna(method='ffill')

# %%

# 直後の値で埋める方法(backward fillの略)
df.fillna(method='bfill')

# %%

# limitで連続する欠損値を何個まで処理するか指定する
df.fillna(method='ffill', limit=2).info()

# %%

# 平均値で埋める
df.fillna(df.mean()).head(10)

# %%

# 中央値で埋める
df.fillna(df.median()).head(10)


# %%

# 最貧値で埋める
df.fillna(df.mode()).head(10)


# %%

#個別に値で埋める