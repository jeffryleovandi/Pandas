##13: Konversi nilai numerik ke dalam sejumlah kategori
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 10
n_cols = 1
cols = ('usia',)

df = pd.DataFrame(np.random.randint(1, 99, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Pengelompokkan nilai numerik ke dalam beberapa kategori menggunakan cut()
df['kelompok_usia'] = pd.cut(df['usia'], 
                             bins=[0, 18, 65, 99], 
                             labels=['anak', 'dewasa', 'manula'])
df

##14: Menggabungkan (merge) dua Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
                  columns=cols)
df
df1 = df.copy(deep=True)
df1 = df1.drop([1, 4])
df1
df2 = df.copy(deep=True)
df2 = df2.drop([0, 3])
df2

#Menggabungkan dua Data Frame
df_inner = pd.merge(df1, df2, how='inner')
df_inner
df_outer = pd.merge(df1, df2, how='outer')
df_outer

##15: Memecah nilai string dari suatu kolom ke dalam beberapa kolom baru
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
data = {'nama':['Didi Kempot', 'Glenn Fredly', 'Mbah Surip'], 
        'tempat_kelahiran':['Surakarta, Jawa Tengah', 'Jakarta, DKI Jakarta', 'Mojokerto, Jawa Timur']}
df = pd.DataFrame(data)
df

#Memecah nama depan dan nama belakang
df[['nama_depan', 'nama_belakang']] = df['nama'].str.split(' ', expand=True)
df
#Memecah nama kota dan propinsi
df[['kota', 'propinsi']] = df['tempat_kelahiran'].str.split(',', expand=True)
df

##16: Menata ulang Data Frame dengan mutiple indexes menggunakan unstack()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Data Frame dengan multiple indexes dari hasil groupping
df.groupby(['sex', 'pclass'])['survived'].mean().to_frame()

#Menata ulang Data Frame dengan mutiple indexes
df.groupby(['sex', 'pclass'])['survived'].mean().unstack()