import numpy as np
# from matplotlib import pyplot
import matplotlib.pyplot

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')

line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance

def onpick(event):
    ind = event.ind
    print('selected points:', ind)

fig.canvas.mpl_connect('pick_event', onpick)

matplotlib.pyplot.show()
