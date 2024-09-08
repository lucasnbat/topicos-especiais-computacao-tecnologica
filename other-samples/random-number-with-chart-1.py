import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5) # 5 barras, 250 valores distribuidos entre eles
plt.show()