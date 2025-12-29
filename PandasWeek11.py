##41: Menerapkan agregasi pada sejumlah kolom dengan agg()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Menerapkan agregasi pada sejumlah kolom dengan agg()
df.groupby('pclass').agg({'pclass':'count', 
                          'age':['mean', 'max'], 
                          'survived': 'mean'})
df.groupby('pclass').agg(n_pass=('pclass', 'count'),
                         avg_age=('age', 'mean'),
                         max_age=('age', 'max'), 
                         survival_rate=('survived', 'mean'))

##42: Mengurutkan data berdasarkan kolom tertentu
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Mengurutkan data berdasarkan kolom tertentu
df.sort_values('age').head()
df.sort_values('age', ascending=False).head()
df.sort_values(['survived', 'age']).head()

##43: Menangani whitespace pada Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
data = {'nim': ['10', '11', '12', '13', '  '],
        'nama': ['adi', '  ', 'tejo', '  ', 'bejo']}

df = pd.DataFrame(data)
df

#Menangani whitespace pada Data Frame
df
df.info()
df = df.replace(r'^\s*$', np.nan, regex=True)
df
df.info()

##44: Menata ulang penempatan kolom pada Data Frame
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

#Menata ulang penempatan kolom pada Data Frame
df[['D', 'C', 'A', 'E', 'B']]
df
df = df[['D', 'C', 'A', 'E', 'B']]
df