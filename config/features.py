import pandas as pd

df=pd.read_csv('model/Training (1).csv')

features = df.drop(columns='prognosis').columns