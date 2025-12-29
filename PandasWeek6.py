##21: Melakukan agregasi menggunakan agg()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/Iris.csv')
df

#Mengenal groupby() dan fungsi agregasi
df.groupby('Species')['PetalLengthCm'].count().to_frame()
df.groupby('Species')['PetalLengthCm'].mean().to_frame()
df.groupby('Species')['PetalLengthCm'].median().to_frame()

#Agregasi dengan agg()
df.groupby('Species')['PetalLengthCm'].agg(['count', 'mean', 'median'])
#Agregasi dengan describe()
df.groupby('Species')['PetalLengthCm'].describe()

##22: Memantau penggunaan memory suatu Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df_titanic = pd.read_csv('./data/titanicfull.csv')
df_titanic.head()
df_iris = pd.read_csv('./data/Iris.csv')
df_iris.head()

#Memantau penggunaan memory suatu Data Frame
df_titanic.info(memory_usage='deep')
df_iris.info(memory_usage='deep')
#Memantau penggunaan memory untuk setiap kolom dari suatu Data Frame
df_titanic.memory_usage(deep=True)
df_iris.memory_usage(deep=True)

##23: Seleksi baris pada Data Frame dengan query()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'kolom_satu':[1, 2, 3, 4, 5], 
     'kolom dua':[10, 20, 30, 40, 50]}
df = pd.DataFrame(d)
df
#Seleksi baris dengan query()
df.query('kolom_satu > 2')
df.query('`kolom dua` > 30')

##24: UTC dan konversi zona waktu (time zone) pada Python Pandas
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Series
s = pd.Series(range(1591683521, 1592201921, 3600))
s = pd.to_datetime(s, unit='s')
s.head()
#Unix Epoch Time
#Epoch Time Converter

#Pengaturan zona waktu (time zone)
s = s.dt.tz_localize('UTC')
s.head()
s = s.dt.tz_convert('Asia/Jakarta')
s.head()
s = s.dt.tz_convert('Australia/Hobart')
s.head()