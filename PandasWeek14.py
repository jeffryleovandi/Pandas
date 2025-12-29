##53: Membuat kategori baru berdasarkan threshold (ambang batas)
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'hobi':['jogging', 'mancing', 'renang',
             'mancing', 'mancing', 'baca', 
             'baca', 'mancing', 'fotograsi', 
             'mancing', 'camping']}

df = pd.DataFrame(d)
df

#Membuat kategori baru berdasarkan threshold (ambang batas)
df['hobi'].value_counts()
persentase = df['hobi'].value_counts(normalize=True)
persentase
threshold = 0.1
hobi_lain = persentase[persentase < threshold].index
hobi_lain
df['hobi'] = df['hobi'].replace(hobi_lain, 'lainnya')
df['hobi']
df['hobi'].value_counts(normalize=True)

##54: Menyimpan Data Frame sebagai file CSV
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
data = {'nama' : ['bayu', 'indra', 'devi', 'agni'], 
        'jenis kelamin' : ['L', 'L', 'P', 'L'], 
        'usia' : [23, 21, 22, 25]}

df = pd.DataFrame(data) 
df

#Menyimpan Data Frame sebagai file CSV
df.to_csv('data_peserta.csv')
df = pd.read_csv('data_peserta.csv')
#df = pd.read_csv('data_peserta.csv'), index_col = 0

df

##55: Menghitung jumlah baris menurut kriteria tertentu
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)
#1.0.5
#1.18.5

#Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size= (n_rows, n_cols)), columns=cols)
df

#Menghitung jumlah baris menurut kriteria tertentu
(df['A'] < 5).sum()
(df['A'] < 5).mean()

##56: Mengeluarkan kolom dari Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
data = {'nama' : ['bayu', 'indra', 'devi', 'agni'], 
        'jenis kelamin' : ['L', 'L', 'P', 'L'], 
        'usia' : [23, 21, 22, 25]}

df = pd.DataFrame(data) 
df

#Mengeluarkan kolom dari Data Frame
usia = df.pop('usia').to_frame()
df
usia 