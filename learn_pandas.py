import pandas as pd 
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
df = pd.read_csv('C:\ML\warung.csv', delimiter = ';')

# seting index

df = df.set_index('Date')
print('seting index : \n', df.head(10))

# slicing 

print(df[0:20])
# masking
print('masking : \n',df[(df['# of Orders'] > 100) & (df['# of Orders'] < 200)])                            
# indexer loc , iloc, and ix
print(df.iloc[0:5])
print('mwmilih kolom dan baris menggunakn iloc : \n',df.iloc[:5, :3])
# memilih kolom
print('memilih kolom : \n',df['# of Orders'].head())
print('memilih kolom dengan cara lain : \n', df.Service.head())

#Transpose data farem
print(df.T)

# agregation dan menambah kolom baru 
df['kolom baru']= df['# of Orders']*100
df['kolom_baru_1'] = df['# of Orders']/df['kolom baru']
print(df.head())

# mengambil nilai dari data frame
print(df.values)
# mengakses values dari data frame dan indexing
print('indexing setelah values :\n', df.values[3])

'operasi data di pandas'
print('\n')
rng = np.random.RandomState(42)
# data time series
ser = pd.Series(rng.randint(0, 10, 4))
# data frame crostabe
data = pd.DataFrame(rng.randint(1, 10, (3,4)), 
                    columns=['a','b','c','d'])

# Handling Mising Data

