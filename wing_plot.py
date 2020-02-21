#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:45:57 2020

@author: neelappagouda
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def wing_plot(number):

    """
    This module is meant to plot the highest rms value airfoils from
    the set of airfoils.

    input: index corresponding to highest rms value airfoil
    output: single plot representing all maximum perturbed airfoils

    """

    for i in range(number):


        with open('output_files/perturbed_wing/wing_{}.csv'.format( i + 1 ),'r') as f:
            adf = np.loadtxt(f)

            adf = np.transpose(adf)


            X = adf[0]
            Y = adf[1]
            Z = adf[2]

            fig = plt.figure()
            ax = Axes3D(fig)
            ax.plot3D(X, Z, Y, 'r,')
            ax.set_xlabel("x"); ax.set_ylabel("z"); ax.set_zlabel("y")
            ax.set_aspect(aspect="auto",adjustable="datalim")
            #plt.xlim( 0.08 , -0.08 )
            ax.grid(False)
            #plt.grid(b=None)
            #ax.view_init(elev =-90, azim = 0)
            #ax.view_init(elev = 0, azim = -180)
            plt.savefig('output_files/fig_wing/wing_{}.png'.format( i + 1 ),dpi = 300)
        #    fig.set_title('surface')
        plt.show()


wing_plot(20)
