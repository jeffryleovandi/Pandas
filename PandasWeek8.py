##29: Melakukan random sampling pada Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'col_1':[1, 2, 3, 4, 5], 
     'col_2':[10, 20, 30, 40, 50]}
df = pd.DataFrame(d)
df

#Random sampling with/without replacement
df.sample(n=4, replace=False, random_state=0)
df.sample(n=4, replace=True, random_state=0)

##30: Akses nilai variabel pada query()
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

#Akses nilai variabel pada query()
df.query('A > 10')
rerata = df['A'].mean()
rerata
df.query('A > @rerata')

##31: Mengenal tipe data ordinal pada Pandas
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'pelanggan':[11, 12, 13, 14], 
     'kepuasan':['baik', 'cukup', 'buruk', 'cukup']}

df = pd.DataFrame(d)
df

#Tipe data ordinal pada Pandas
from pandas.api.types import CategoricalDtype

tingkat_kepuasan = CategoricalDtype(['buruk', 'cukup', 'baik', 'sangat baik'], 
                                    ordered=True)

df['kepuasan'] = df['kepuasan'].astype(tingkat_kepuasan)
df
df = df.sort_values('kepuasan', ascending=True)
df
df[df['kepuasan'] >= 'cukup']

##32: Plotting dari suatu Pandas Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 40
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
                  columns=cols)
df.head()

#Line Plot
df.head()
df.plot(kind='line')
df[['A', 'B']].plot(kind='line')

#Bar Plot
df.head()
df.plot(kind='bar')
df[['A', 'B']].plot(kind='bar')
df[['A', 'B']].head().plot(kind='bar')
df[['A', 'B']].head().plot(kind='barh')

#Area Plot
df.head()
df.plot(kind='area')
df[['A', 'B']].head().plot(kind='area')

#Box Plot
df.head()
df.plot(kind='box')

#Histogram
df.head()
df.plot(kind='hist')
df[['A', 'B']].plot(kind='hist')

#Kernel Density Estimation (KDE)
df.head()
df.plot(kind='kde')

#Scatter Plot
df.head()
df.plot(x='A', y='B', kind='scatter')