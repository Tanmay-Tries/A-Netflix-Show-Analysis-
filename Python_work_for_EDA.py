import numpy as np
import pandas as pd
import Matplotlib.pyplot as plt
import Seaborn as sns

df = pd.read_csv('/content/mymoviedb.csv', lineterminator='\n')

df.head(5)

df.info()

df['Genre'].head(5)

df.duplicated().sum()

df.describe()

#Original_Language col is droped
df=df.drop(['Original_Language'],axis=1)
df.head(5)

#Converting Realease Date (an object datatype) to date time 
df['Release_Date']=pd.to_datetime(df['Release_Date'])

df['Release_Date'].head(5)
print(df['Release_Date'].dtype
     
df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtype)

df.head(5)

#list of cloumns to drop
list=['Overview','Poster_Url']

df=df.drop(list,axis=1)\
df.head(5)

def categorise_col(df,col,labels):
  edges=[df[col].describe()['min'],
         df[col].describe()['25%'],
         df[col].describe()['50%'],
         df[col].describe()['75%'],
         df[col].describe()['max']]

  df[col]=pd.cut(df[col],edges,labels=labels,duplicates='drop')
  return df

labels=['not_popular','below_avg','average','popular']

categorise_col(df,'Vote_Average',labels)

df['Vote_Average'].value_counts()

df.dropna(inplace=True)

df.isna().sum()

#Splitting the Genre and then exploding to clear the genres so there will be ony one genre per movie
df['Genre'] = df['Genre'].astype(str).str.split(',')
df = df.explode('Genre').reset_index(drop=True)
df['Genre'] = df['Genre'].str.strip()
df['Genre'] = df['Genre'].replace('nan', pd.NA)
df = df.dropna(subset=['Genre'])

df.head(5)

#Casting Columns into Category
df['Genre']=df['Genre'].astype('category')
df['Genre'].dtypes
df.info()

#Data Visualization
