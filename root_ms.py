#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:51:52 2020

@author: neelappagouda
"""
import numpy as np


def root_mean_square ( iteration ):
    
    """
    This module find the rms value between two wing coordinates.

    input: None
    output: RMS value into the file.
    """

    with open('output_files/perturbed_wing/wing_{}.csv'.format( iteration ), 'r') as X_new:
        with open('output_files/initial_wing.csv', 'r') as X_old:
            
            perturbed_wing = np.loadtxt( X_new )
            initial_wing   = np.loadtxt( X_old )

            diff = perturbed_wing - initial_wing 

    Rms_x = np.sqrt( np.mean( diff[:, 0] ** 2) )
    
    Rms_y = np.sqrt( np.mean( diff[:, 1] ** 2) )
    
    Rms_z = np.sqrt( np.mean( diff[:, 2] ** 2) )

    with open('output_files/Root_ms.csv', 'a') as r:
        r.write('{0} \t \t {1} \t \t {2} \n'.format( Rms_x, Rms_y, Rms_z ))
