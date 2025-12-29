##05: Membalik urutan baris dan kolom pada Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Membalik urutan kolom
df.loc[:, ::-1]
#Membalik urutan baris
df.loc[::-1]
#Membalik urutan baris dan melakukan penyesuaian ulang index
df.loc[::-1].reset_index(drop=True)

##06: Mengganti nama (label) kolom pada Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Mengganti nama (label) untuk sebuah kolom pada Data Frame
df.rename(columns={'C':'Hobi'})
#Mengganti nama (label) untuk banyak kolom pada Data Frame
df.rename(columns={'A':'Nama', 'B':'Alamat', 'D':'Kota'})

##07: Menghapus (drop) missing values (NaN)
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
## DEPRICATED ##
# df = pd.util.testing.makeMissingDataframe().reset_index() 
# df.head()
n_rows = 30
n_cols = 4
cols = ['A', 'B', 'C', 'D']

df = pd.DataFrame(np.random.randn(n_rows, n_cols), columns=cols)

nan_mask = np.random.rand(n_rows, n_cols) < 0.2
df[nan_mask] = np.nan

df = df.reset_index()
df.head()
df = df.rename(columns={'index':'Z'})
df.head()
df_backup = df.copy(deep=True)

#Menghapus (drop) setiap kolom yang mengandung missing values
df = df.dropna(axis='columns') 
df.head()
#Menghapus (drop) setiap baris yang mengandung missing values
df = df_backup.copy(deep=True)
df = df.dropna(axis='rows')
df.head()

#Persentase missing values untuk tiap kolom
df = df_backup.copy(deep=True)
df.isna().mean()
#Menghapus (drop) setiap kolom yang mengandung missing values berdasarkan threshold
treshold = len(df) * 0.9
df = df.dropna(thresh=treshold, axis='columns')
df.head()

##08: Memeriksa kesamaan antar dua buah kolom (Series) pada Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
data = {'A':[15, 15, 18, np.nan, 12], 
        'B':[15, 15, 18, np.nan, 12]}

df = pd.DataFrame(data)
df

#Mengenal Pandas Series
df['A']
type(df['A'])
type(df)

#Memeriksa kesamaan dengan operator ==
df['A'] == df['B']
#Memeriksa kesamaan dengan method equals()
df['A'].equals(df['B'])
#Memeriksa kesamaan antar dua Data Frame
df1 = df.copy(deep=True)

df.equals(df1)
df == df1