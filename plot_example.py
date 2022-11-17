import matplotlib

# NB: here fix backend

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

print(matplotlib.get_backend())

x = np.linspace(0,2*np.pi,10000)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(np.pi/12))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))

plt.show()