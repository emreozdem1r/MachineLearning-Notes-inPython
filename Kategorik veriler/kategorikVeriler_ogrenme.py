# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:36:37 2019

@author: Emre
"""

#nominal veriler: sıralama olur ancak ölçüm belirtmez(büyüktür küçüktür gibi)
#ordinal veriler: sıralama imkanı olan veriler

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler1= pd.read_csv('veriler.csv')

print(veriler1)
#veri ön işleme
boy=veriler1[['boy']]
print(boy)

boykilo=veriler1[['boy','kilo']]
print(boykilo)

veriler=pd.read_csv('eksikveriler.csv')

#print(veriler)

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy='mean',axis=0)

Yas=veriler.iloc[:,1:4].values
#print(Yas)

imputer=imputer.fit(Yas[:,1:4])

Yas[:,1:4] = imputer.transform(Yas[:,1:4])
#print(Yas)

ulke=veriler.iloc[:,0:1].values
#print(ulke)
#çevrimi yapıyoruz
from sklearn.preprocessing import LabelEncoder
#labelEncoder her bir değer için sayısal değer üretir
le=LabelEncoder()
ulke[:,0]=le.fit_transform(ulke[:,0])
print(ulke)
#0-1-2 gibi dönüştürdü. Sadece 0 ve 1 lerden oluşacak

from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
#print(ulke)

sonuc=pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])
print(sonuc)

sonuc2=pd.DataFrame(data=Yas, index=range(22),columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet=veriler.iloc[:,4].values
print(cinsiyet)
sonuc3=pd.DataFrame(data=cinsiyet, index=range(22),columns=['cinsiyet'])
print(sonuc3)

#concat 2 tane dataframe'i birleştirir
#axis=1 olması verileri anlamlı hale getirmek amaçlı

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([sonuc,sonuc3],axis=1)
print(s2)

