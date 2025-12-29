##09: Membagi Data Frame menjadi dua secara acak
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Membagi Data Frame menjadi dua secara acak berdasarkan proporsi tertentu
df.shape
proporsi = 0.7
df_1 = df.sample(frac=proporsi)
df_2 = df.drop(df_1.index)

print(f'df_1 shape: {df_1.shape}')
print(f'df_2 shape: {df_2.shape}')
df_1
df_2

##10: Mengganti nama (label) kolom pada Data Frame berdasarkan pola
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.columns = ['Pclass', 'Survival status', 'full Name', 'Sex  ', '  Age', 
              'Sib SP', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
df_backup = df.copy(deep=True)

df.head()

#Menggunakan lowercase untuk nama kolom dan mengganti spasi dengan _
df.columns = df.columns.str.replace(' ', '_').str.lower()
df.head()
#Memangkas kelebihan spasi pada nama kolom
df = df_backup.copy(deep=True)

df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
df.head()

##11: Melakukan seleksi kolom dan baris pada Data Frame menggunakan loc
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Seleksi kolom dan baris menggunakan loc
df.loc[[0,3,4], ['B','E']]
#Seleksi baris dengan kondisi
df.loc[df['B']>10, ['B','D','E']]
#Slicing Data Frame dengan loc
df.loc[0:4, 'B':'D']

##12: Membentuk kolom bertipe datetime dari sejumlah kolom lain pada Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
data = {'day':[1, 2, 10 ,25, 12], 
        'month':[1, 2, 4, 5, 6], 
        'year':[2000, 2001, 2010, 2015, 2020]}

df = pd.DataFrame(data)
df

#Membentuk kolom bertipe datetime
df['penaggalan'] = pd.to_datetime(df[['day', 'month', 'year']])
df
df.dtypes