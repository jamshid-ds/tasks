import pandas as pd
import numpy as np

!git clone https://github.com/MansurCompAI/Practicum_Datasets.git

data15 = pd.read_csv("/content/Practicum_Datasets/Happiness/2015.csv")
data16 = pd.read_csv("/content/Practicum_Datasets/Happiness/2016.csv")
data17 = pd.read_csv("/content/Practicum_Datasets/Happiness/2017.csv")
data18 = pd.read_csv("/content/Practicum_Datasets/Happiness/2018.csv")
data19 = pd.read_csv("/content/Practicum_Datasets/Happiness/2019.csv")

data15.head()
data16.head()
data17.head()
data18.head()
data19.head()

df15 = pd.pivot_table(data15, index=['Region','Country'])
df16 = data16.set_index(['Region', 'Country'])
print(f"2015 yil ma'lumolar to'plami\n {df15.index}\n")
print(f"2016 yil ma'lumolar to'plami\n {df16.index}")

df15.head()

df16.head()

we_2015 = df15.loc["Western Europe"]
we_2016 = df16.loc["Western Europe"]


def extractor(dataframe):
  columns = ['Country', 'Country or region', 'Happiness Rank', 'Happiness.Rank','Overall rank', 'Happiness Score','Happiness.Score', 'Score']
  mask = [col for col in dataframe.columns if col in columns]
  return dataframe[mask]

dataframes = [data15, data16, data17, data18, data19]
data15, data16, data17, data18, data19 = [extractor(dataframe) for dataframe in dataframes]

columns = ['Country', 'Happiness Rank', 'Happiness Score']

data17.columns = columns 
data18 = data18[['Country or region', 'Overall rank', 'Score']] 
data18.columns = columns

data19 = data19[['Country or region', 'Overall rank', 'Score']] 
data19.columns = columns

