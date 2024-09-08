# train/ test

# Treinar/Teste é um método para medir a precisão do seu modelo.
# É chamado de Treinamento/Teste porque você divide o conjunto de dados em dois
# conjuntos: um conjunto de treinamento e um conjunto de teste.
# 80% para treinamento e 20% para teste.
# Você treina o modelo usando o conjunto de treinamento.
# Você testa o modelo usando o conjunto de testes.
# Treinar
# o modelo significa criar o modelo.
# Testar o modelo significa testar a precisão do modelo.

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

plt.scatter(test_x, test_y)
plt.show()
