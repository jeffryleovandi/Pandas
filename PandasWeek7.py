##25: Pengaturan tampilan (display option) pada Python Pandas
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df

#Pengaturan tampilan
pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_colwidth', 20)

df
pd.reset_option('^display.', silent=True)

df
pd.describe_option()

##26: Membuat Data Frame dari hasil seleksi Spreadsheet
#Import Modules
import pandas as pd

print(pd.__version__)

#Membuat Data Frame dari hasil seleksi Spreadsheet
# df = pd.read_clipboard()
# df

##27: Mengenal fungsi agregasi first() dan last()
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'dokter':['Budi', 'Wati', 'Iwan', 'Budi', 'Budi', 'Wati'], 
     'pasien':['Abdul', 'Rahmat', 'Asep', 'Joko', 'Wiwin', 'Lisa']}

df = pd.DataFrame(d)
df

#Mengenal fungsi agregasi first() dan last()
df.groupby('dokter')['pasien'].count().to_frame()
df.groupby('dokter')['pasien'].first().to_frame()
df.groupby('dokter')['pasien'].last().to_frame()

##28: Mengenal explode dan implode list pada Data Frame
#Import Modules
import pandas as pd

print(pd.__version__)

#Persiapan Data Frame
d = {'Team':['DC', 'Marvel'], 
     'Heroes':[['Batman', 'Superman', 'Wonder Woman', 'Aquaman', 'Green Lantern', 'Shazam'], 
               ['Iron Man', 'Captain America', 'Ant-Man', 'Black Panther', 'Captain Marvel']]}

df = pd.DataFrame(d)
df

#Explode
df1 = df.explode('Heroes')
df1

#Implode
d = {'Team':['DC', 'Marvel']}
df2 = pd.DataFrame(d)
df2
df2['Imploded'] = df1.groupby(df1.index)['Heroes'].agg(list)
df2