"""
Source-Sink
"""

import math
import numpy
from matplotlib import pyplot


N=20                          #total grid points in each direction
x_start, x_end = -2.0, 2.0    # x direction boundaries
y_start, y_end = -2.0, 2.0    # y direction boundaries
x = numpy.linspace(x_start,x_end,N)  # 1D array of x co-ordinates
y = numpy.linspace(y_start,y_end,N)  # 1D array of y co-ordinates

X, Y = numpy.meshgrid(x, y)   # generate grid


x_s, y_s = -1.0, 0.0          # source location
S_str = 5.0                   # source strength

# radial distance and angle from source
r   = numpy.sqrt( (X-x_s)**2 + (Y-y_s)**2)
phi = numpy.arctan2(Y-y_s, X-x_s)

# velocity field
u = numpy.cos(phi)*S_str/r
v = numpy.sin(phi)*S_str/r

# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
pyplot.figure(figsize=(width, height))
pyplot.xlabel('x', fontsize=16)
pyplot.ylabel('y', fontsize=16)
pyplot.xlim(x_start, x_end)
pyplot.ylim(y_start, y_end)
pyplot.quiver(X, Y, u, v)
pyplot.scatter(x_s, y_s,
               color='#CD2305', s=80, marker='o');
