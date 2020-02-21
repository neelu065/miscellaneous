#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:01:54 2020

@author: neelappagouda
"""


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import axes3d, Axes3D
number = 1
for i in range(number):
    
    
    with open('perturbed_wing/wing_{}.csv'.format( i + 1 ),'r') as f:
        adf = np.loadtxt(f)
        
    adf = np.transpose(adf)
    
        
    X = adf[0]
    Y = adf[1]
    Z = adf[2]
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter3D(X, Z , Y, '.')
    
    with open('initial_wing.csv','r') as f:
        adf = np.loadtxt(f)
    
    adf = np.transpose(adf)

    
    X = adf[0]
    Y = adf[1]
    Z = adf[2]
    ax.scatter3D(X, Z, Y, '.')
    #ax.view_init(elev = 0, azim = -180)
    ax.view_init(60 , 35)
    plt.savefig('fig_wing/wing_{}.png'.format( i + 1 ),dpi = 300)
#    fig.set_title('surface')
plt.show()


number = 1