##49: Seleksi kolom dengan f-string
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/Iris.csv')
df.head()

#Seleksi kolom dengan f-string
df['SepalWidthCm'].to_frame().head()
part = 'Sepal'

df[f'{part}WidthCm'].to_frame().head()
df[['PetalWidthCm', 'PetalLengthCm']].head()
part = 'Petal'

df[[f'{part}WidthCm', f'{part}LengthCm']].head()

##50: Membuat kolom baru dengan looping dan f-string
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'penjual':['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'], 
     'barang':['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']}

df = pd.DataFrame(d)
df

#Membuat kolom baru dengan for loop dan f-string
cols = ['penjual', 'barang']

for col in cols:
    df[f'count_tiap_{col}'] =  df.groupby(col).cumcount() + 1
    
df

##51: Seleksi baris dengan between()
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)
#2.2.2
#1.26.4

#Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Seleksi baris dengan between()
df[df['A'].between(2, 5)]

## DEPRICATED ##
# df[df['A'].between(2, 5, inclusive=False)]
df[df['A'].between(2, 5, inclusive='left')]
df[df['A'].between(2, 5, inclusive='right')]
df[df['A'].between(2, 5, inclusive='both')]
df[df['A'].between(2, 5, inclusive='neither')]

##52: Transformasi kolom menjadi baris pada Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {
'kode_area': [123, 456, 789, 321],
'pabrik': [4, 2, 5, 0],
'gudang': [2, 4, 7, 3],
'toko': [64, 32, 15, 24]
}

df = pd.DataFrame(d)
df

#Transformasi kolom menjadi baris
df = df.melt(id_vars='kode_area', 
             var_name='jenis_bangunan', 
             value_name='jumlah')
df