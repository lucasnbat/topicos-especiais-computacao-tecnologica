import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv", delimiter=';')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedC02 = regr.predict([[3300, 1300]])

print(predictedC02)

# Previmos que um carro com motor de 1,3 litro e peso de 3.300 kg liberará 
# aproximadamente 115 gramas de CO2 por cada quilômetro percorrido.
# O que mostra que o coeficiente de 0,00755095 está correto:
# 107,2087328 + (1000 * 0,00755095) = 114,75968
