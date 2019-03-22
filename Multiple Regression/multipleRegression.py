#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri Onisleme

#2.1. Veri Yukleme
veriler = pd.read_csv('veriler.csv')

#encoder:  Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

#cinsiyet kolonunun sayısal veriye dönüştürülmesi
c = veriler.iloc[:,-1:].values
print(c)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
c[:,0] = le.fit_transform(c[:,0])
print(c)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
c=ohe.fit_transform(c).toarray()
print(c)
#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=['fr','tr','us'] )
print(sonuc)

sonuc2 =pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

sonuc3 = pd.DataFrame(data = c[:,:1] , index=range(22), columns=['c'])
print(sonuc3)

#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2= pd.concat([s,sonuc3],axis=1)
print(s2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

#cinsiyet tahmininde bulunması için x_train ve y_train değişkenlerini fit fonksiyonuna veriyoruz.
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

#tahminde bulunma cinsiyet için
y_pred=regressor.predict(x_test)
#boy sütununun tablodan çekilmesi
#kalan tablodan train ve testler oluşturarak boy tahminde bulunma
boy=s2.iloc[:,3:4].values
sol=s2.iloc[:,:3]
sag=s2.iloc[:,4:]
veri=pd.concat([sol,sag],axis=1)

#boy tahmini için train ve test değişkenlerini üretiyoruz
x_train,x_test,y_train,y_test=train_test_split(veri,boy,test_size=0.33,random_state=0)

#x_train ve y_train değişkenlerini fit fonksiyonuna verip boy tahmininde bulunmasını sağlıyoruz.
regression2=LinearRegression()
regression2.fit(x_train,y_train)
y_pred=regression2.predict(x_test)
    
    

