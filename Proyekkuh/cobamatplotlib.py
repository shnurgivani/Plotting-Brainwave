from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#+,- = np.loadtxt('data.csv', unpack = True, delimiter = ',')
x,y = np.loadtxt('hore.csv', unpack = True, delimiter = ',')

#print (x)
#print (y)

plt.plot(x,y)
plt.title('Brainwave data result')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.savefig('Gelombang.png')
