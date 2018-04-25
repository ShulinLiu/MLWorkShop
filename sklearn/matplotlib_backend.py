# reference from:
# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python

# two other reference:
# https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
# 

# set back-end
# solution 1:
# add "backend: TkAgg" to ~/.matplotlib/matplotlibrc


# solution 2:
import matplotlib as mpl
mpl.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# # Plot the points using matplotlib
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show() # You must call plt.show() to make graphics appear.


# subplot
plt.subplot(2,1,1)

plt.plot(x,y_sin)
plt.title('Sine')

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')
plt.show()