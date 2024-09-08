import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(5.0, 1.0, 100000)

plt.hist(x, 100) # 5 barras, 250 valores distribuidos entre eles
plt.show()