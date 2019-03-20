
#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri Onisleme

#2.1. Veri Yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")

print(veriler)
#Aylar ve satislar sütunlarının değişkenlerde tutulması

aylar=veriler[['Aylar']]
satislar=veriler[['Satislar']]

print(aylar)
print(satislar)


#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

# model inşası(linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

#burada x_test üzerinden tahminlerini yapıyor.
tahmin=lr.predict(x_test)

# x_train ve y_train değişkenleri dağınık halde bulunduğu için bunları sıralıyoruz.

x_train=x_train.sort_index()
y_train=y_train.sort_index()

plt.plot(x_train,y_train)

#y=ax+b doğrusunu oluşturduğu tahmine göre çiziyor.
plt.plot(x_test,lr.predict(x_test))

plt.title("Aylara göre satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
    

