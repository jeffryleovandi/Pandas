##37: Seleksi baris dengan banyak kriteria
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Seleksi baris dengan banyak kriteria
df[(df['sex']=='female') & (df['age']>=60) & (df['embarked']=='S') & (df['survived']==1)]
df[
    (df['sex']=='female') & 
    (df['age']>=60) & 
    (df['embarked']=='S') & 
    (df['survived']==1)
]
kr1 = df['sex']=='female'
kr2 = df['age']>=60
kr3 = df['embarked']=='S'
kr4 = df['survived']==1

df[kr1 & kr2 & kr3 & kr4]

##38: Mengenal parameter header dan skiprows
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/iris_error.csv')
df.head(8)
df = pd.read_csv('./data/iris_error.csv', header=2, skiprows=[5,6])
df.head()

##39: Mengacak urutan baris pada DataFrame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 6
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 5, size=(n_rows, n_cols)), 
                  columns=cols)
df

#Mengacak urutan baris pada DataFrame
df.sample(frac=1.0, random_state=1)
df.sample(frac=1.0, random_state=1).reset_index(drop=True) 

##40: Mengakses sekelompok data dengan get_group()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.head()

#Mengakses sekelompok data yang sudah terkelompok dengan get_group()
grouped_df = df.groupby('sex')
grouped_df.get_group('female').head(10)
grouped_df = df.groupby('survived')
grouped_df.get_group(1).head(10)