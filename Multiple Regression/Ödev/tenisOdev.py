# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:33:06 2019

@author: Emre
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler=pd.read_csv("odev_tenis.csv")
print(veriler)

outlook=veriler.iloc[:,0:1].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
outlook[:,0]=le.fit_transform(outlook[:,0])
print(outlook)
veriler2=veriler.iloc[:,3:5]
veriler2=veriler2.apply(LabelEncoder().fit_transform)


from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features="all")
cOutlook =ohe.fit_transform(outlook).toarray()
print(cOutlook)

sonuc=pd.DataFrame(data=cOutlook, index = range(14),columns = ['s','r','o'])
print(sonuc)

combine=pd.concat([sonuc,veriler2],axis=1)
print(combine)
hum=veriler.iloc[:,2:3]
combine=pd.concat([combine,hum],axis=1)
temp=veriler.iloc[:,1:2]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=  train_test_split(combine,temp,test_size=0.33,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred= regressor.predict(x_test)


























