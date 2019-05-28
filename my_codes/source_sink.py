# -*- coding: utf-8 -*-
"""
Source-Sink
"""

import math
import numpy
from matplotlib import pyplot


N=50                          #total grid points in each direction
x_start, x_end = -2.0, 2.0    # x direction boundaries
y_start, y_end = -2.0, 2.0    # y direction boundaries
x = numpy.linspace(x_start,x_end,N)  # 1D array of x co-ordinates
y = numpy.linspace(y_start,y_end,N)  # 1D array of y co-ordinates


X, Y = numpy.meshgrid(x, y)   #generate grid

# plot grid
width = 10.0                  #graph width on screen in cm
height = (y_end - y_start) / (x_end - x_start) * width #graph height
pyplot.figure(figsize=(width, height)) #create figure
pyplot.xlim(x_start, x_end) 
pyplot.ylim(y_start, y_end)
pyplot.scatter(X, Y, s=5, color='blue', marker='o')

