#  Preveja a emissão de CO2 de um carro de 1,3 litro que pesa 2.300 kg:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data.csv", delimiter=";")

X = df[['Weight', 'Volume']]
y = df['CO2']

# transforma/dimensiona os valores X
scaledX = scale.fit_transform(X) 

# invoca o objeto de regr. linear
regr = linear_model.LinearRegression() 

# executa a mesma coisa mas usando os valores X dimensionados
regr.fit(scaledX, y) 

# executa nova transformação dos valores e guarda em scaled
scaled = scale.transform([[2300,1.3]]) 

# usa o predict da biblioteca de regressão para predizer com base 
# nos valores x e y dimensionados
predictedCO2 = regr.predict([scaled[0]]) 
print (predictedCO2)