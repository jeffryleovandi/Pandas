##45: Memadukan loc dan iloc untuk melakukan seleksi data
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Memadukan loc dan iloc untuk melakukan seleksi data
df.iloc[15:20, :].loc[:, 'name':'age']
df.loc[:, 'name':'age'].iloc[15:20, :]

##46: Seleksi weekdays dan weekends pada data deret waktu (time series)
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
## DEPRECATED ##
# n_rows = 365
# n_cols = 2
# cols = ['col1', 'col2']

# df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
#                   columns=cols)

# df.index = pd.util.testing.makeDateIndex(n_rows, freq='D')
# df
n_rows = 365
n_cols = 2
cols = ['col1', 'col2']

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')

print(df)

#Seleksi weekdays dan weekends
weekdays_df = df[df.index.dayofweek.isin([0, 1, 2, 3, 4])]
weekdays_df.head(7)
weekends_df = df[df.index.dayofweek.isin([5, 6])]
weekends_df.head(7)

##47: Deteksi dan penanganan kolom dengan tipe data beragam (mixed data types)
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'nama':['bejo', 'tejo', 'wati', 'tiwi', 'cecep'], 
     'ipk':[2, '3', 3, 2.75, '3.25']}
df = pd.DataFrame(d)
df

#Deteksi dan penanganan kolom dengan tipe data beragam (mixed data types)
df.dtypes
df['ipk'].apply(type)
df['ipk'].apply(type).value_counts()
df['ipk'] = df['ipk'].astype(float)
df['ipk'].apply(type).value_counts()

##48: Mengenal Cummulative Count dengan cumcount()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'penjual':['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'], 
     'barang':['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']}

df = pd.DataFrame(d)
df

#Mengenal Cummulative Count dengan cumcount()
df['count_tiap_penjual'] = df.groupby('penjual').cumcount() + 1
df
df['count_tiap_barang'] = df.groupby('barang').cumcount() + 1
df
df['count_pasangan_kolom'] = df.groupby(['penjual', 'barang']).cumcount() + 1
df