#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:52:58 2020

@author: neelu
"""

import numpy as np

number_of_wings = 1000

X = [] 


for i in range( number_of_wings ):
    with open( 'output_files/perturbed_wing/unformat_wing/wing_{}.csv'.format( i + 1 ), 'r') as f_read:
        wing = np.loadtxt(f_read)
        for j in range(len(wing) ):
            X.append([wing[j][0] , wing[j][1] , wing[j][2]])
       
X = np.reshape(X, (number_of_wings, len(wing) *3))

s  = np.linalg.svd(X, compute_uv=False)

print(s)
