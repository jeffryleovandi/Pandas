##17: Resampling pada data deret waktu (time series data)
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
## DEPRICATED ##
# n_rows = 365 * 24
# n_cols = 2
# cols = ['col1', 'col2']

# df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
#                   columns=cols)

# df.index = pd.util.testing.makeDateIndex(n_rows, freq='H')
# df
n_rows = 365 * 24 
n_cols = 2         
cols = ['col1', 'col2'] 

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)

df.index = pd.date_range(start='2023-01-01', periods=n_rows, freq='h')

df.head()

#Resampling data dengan interval monthly
df.resample('M')['col1'].sum().to_frame()
#Resampling data dengan interval daily
df.resample('D')['col1'].sum().to_frame()

##18: Membentuk dummy Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Membentuk Data Frame dari Dictionary
pd.DataFrame({'col1':[1, 2, 3, 4], 
              'col2':[5, 6, 7, 8]})
#Membentuk Data Frame dari Numpy Array
n_rows = 5
n_cols = 3

arr = np.random.randint(1, 20, size=(n_rows, n_cols))
arr
pd.DataFrame(arr, columns=tuple('ABC'))

#Membentuk Data Frame dengan memanfaatkan pandas.util.testing
## DEPRICATED ##
# pd.util.testing.makeDataFrame().head()
n_rows = 30 
n_cols = 4 
columns = list('ABCD')

data = np.random.randn(n_rows, n_cols)

df = pd.DataFrame(data, columns=columns)

print(df.head())
## DEPRICATED ##
# pd.util.testing.makeMixedDataFrame().head()
n_rows = 5 

data = {
    'A': np.random.randn(n_rows),                 
    'B': np.arange(1, n_rows + 1),                
    'C': pd.date_range('2024-01-01', periods=n_rows), 
    'D': ['foo', 'bar', 'baz', 'qux', 'quux']    
}

df = pd.DataFrame(data)

print(df.head())
## DEPRICATED ##
# pd.util.testing.makeTimeDataFrame().head()
n_rows = 30  
n_cols = 4   
columns = list('ABCD')  

time_index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')  

df = pd.DataFrame(np.random.randn(n_rows, n_cols), index=time_index, columns=columns)

print(df.head())
## DEPRICATED ##
# pd.util.testing.makeMissingDataframe().head()
n_rows = 5
n_cols = 4

data = np.random.randn(n_rows, n_cols)

df = pd.DataFrame(data, columns=list('ABCD'))

df.iloc[0, 1] = np.nan
df.iloc[2, 3] = np.nan
df.iloc[4, 0] = np.nan

print(df.head())

##19: Formatting tampilan Data Frame
#Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#Persiapan Data Frame
n_rows = 5
n_cols = 2
cols = ['omset', 'operasional']

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), 
                  columns=cols)
df
df['omset'] = df['omset'] * 100_000
df['operasional'] = df['operasional'] * 10_000
df
## DEPRICATED ##
# df.index = pd.util.testing.makeDateIndex(n_rows, freq='D')
# df = df.reset_index()
# df = df.rename(columns={'index':'tanggal'})
# df
n_rows = 365  

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, 2)), columns=['col1', 'col2'])

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')

df = df.reset_index().rename(columns={'index': 'tanggal'})

print(df)

#Melakukan formatting tampilan Data Frame
formatku = {'tanggal':'{:%d/%m/%y}', 
            'operasional':'Rp {:.2f}',
            'omset':'Rp {:.2f}'}

laporan = df.style.format(formatku)
laporan
type(laporan)
# laporan.hide_index()
laporan.set_caption('Data Omset dan Operasional')
## DEPRICATED ##
# laporan.highlight_min('omset', color='pink')
# laporan.highlight_max('omset', color='lightgreen')

# laporan.highlight_min('operasional', color='lightblue')
# laporan.highlight_max('operasional', color='grey')

##20: Menggabungkan (merge) dua Data Frame secara berdampingan
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d1 = {'col1':[1, 2, 3], 
      'col2':[10, 20, 30]}
df1 = pd.DataFrame(d1)
df1
d2 = {'col3':[4, 5, 6], 
      'col4':[40, 50, 60]}
df2 = pd.DataFrame(d2)
df2

#Menggabungkan (merge) dua Data Frame secara berdampingan
df = pd.merge(df1, df2, left_index=True, right_index=True)
df