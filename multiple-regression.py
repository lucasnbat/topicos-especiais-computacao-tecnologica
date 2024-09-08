import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv", delimiter=';')
X = df[['Weight', 'Volume']] # valores independentes, X maíusculo
y = df['CO2'] # valores dependentes, o resultado, y minúsculo

# cria objeto de regressão linear, que possui o metodo fit()
# método toma os valores independentes e dependentes como parametros
# e preenche o objeto de regressão com dados que descrevem o relacionamento
# das variaveis
regr = linear_model.LinearRegression() 
regr.fit(X, y)

# Prever a emissão de CO2 para um carro com peso de 2300kg e volume de 1300cm3
import pandas as pd

# Criar um DataFrame com os mesmos nomes de colunas para evitar o aviso
new_data = pd.DataFrame([[2300, 1300]], columns=['Weight', 'Volume'])

predictedCO2 = regr.predict(new_data)
print(predictedCO2)