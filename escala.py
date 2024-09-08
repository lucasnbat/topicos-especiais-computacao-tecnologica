# Existem diferentes métodos para dimensionar dados, usaremos um método 
# chamado padronização.
# O método de padronização usa esta fórmula:
# z = (x - u) / s

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv", delimiter=";")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

