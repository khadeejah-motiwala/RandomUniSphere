from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math as math
import numpy as np

N= 1000 # number of points on the sphere

theta_array=np.empty(N, float) # initializing an empty numpy array to hold theta coordinates for each point

np.random.seed(42)
for i in range(N):
    theta_array[i]=math.acos(1. - 2.*random.uniform(0.,1.)) #using the cdf of theta in the inverse transform sampling method to obtain random uniform values of theta

phi_array=np.empty((len(theta_array)), float)

for j in range(len(theta_array)):
    phi_array[j]=2.*np.pi*random.uniform(0,1) # using the cdf of phi in the inverse transform sampling method to obtain random uniform values of phi

x = np.sin(theta_array)*np.cos(phi_array) # converting spherical coordinates to cartesian
y = (np.sin(theta_array)*np.sin(phi_array))
z = np.cos(theta_array)

fig = plt.figure(figsize = plt.figaspect(1)) # setting output figure aspect ratio
ax = fig.gca( projection='3d') # creating a 3d figure
ax.scatter(x, y, z, c='r', marker='.') # plotting the points


frame = plt.gca() # create axes

frame.axes.xaxis.set_ticklabels([])
frame.axes.yaxis.set_ticklabels([])
frame.axes.zaxis.set_ticklabels([])

ax.set_xlabel('z')
ax.set_ylabel('y')
ax.set_zlabel('x')


plt.show()