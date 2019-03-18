

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler= pd.read_csv('veri.csv')

print(veriler)

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy='mean',axis=0)
#missing_values= kayıp alanların ne ile ifade edildiği
#iloc fonksiyonuyla 1,2 ve 3. sütundaki değerleri elde ettik
not1=veriler.iloc[:,1:3].values

print(not1)
#fit fonksiyonuyla strategy'i veri üzerine uyguluyoruz
#her kolon için ortalama değer alıyoruz
imputer=imputer.fit(not1[:,1:3])
#transform değiştirme anlamında
not1[:,1:3] = imputer.transform(not1[:,1:3])
#bu şekilde eksik olan veriler yerine ortalama
#değeri yazdırmış olduk
print(not1)