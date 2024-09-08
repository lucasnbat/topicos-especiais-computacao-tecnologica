# O coeficiente é um fator que descreve a relação com uma variável desconhecida.
# Exemplo: se xé uma variável, então 2xé xduas vezes. xé a variável desconhecida e o número 2é o 
# coeficiente.
# Neste caso, podemos solicitar o valor do coeficiente de peso em relação ao CO2 e de volume em relação 
# ao CO2. A(s) resposta(s) que obtemos dizem-nos o que aconteceria se aumentássemos ou diminuíssemos 
# um dos valores independentes.

import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv", delimiter=';')

X = df[['Weight', 'Volume' ] ]
y = df ['CO2']

regr = linear_model.LinearRegression()
regr.fit (X, y)

# imprimindo os coeficientes do objeto LinearRegression()
print (regr.coef_) # [Peso, Volume] = [0.00755095 0.00780526]

# Estes valores dizem-nos que se o peso aumentar em 1kg, a emissão de CO2 
# aumenta em 0,00755095g.
# E se o tamanho do motor (Volume) aumentar em 1 cm 3 , a emissão de CO2 
# aumenta em 0,00780526 g.