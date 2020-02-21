#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:07:59 2020

@author: neelappagouda
"""

import numpy as np

def selection(number):
    
    """
    Here for the given number a vector 
    consisting of maximum rms values is generated
    and returned to further module.
    
    input: number of maximum rms value airfoil to be plotted.
    output: vector corresponding to max_rms_index
    """
    
    with open('output_files/Root_ms.csv', 'r') as f:
        rms_vector = np.loadtxt(f)
        rms_vector = (rms_vector[:,0])
        max_rms_index = []
        
        for i in range(number):
            index = np.argmax(rms_vector)
            print(index)
            max_rms_index.append(index)
            rms_vector[index] = 0
    
    return max_rms_index
    

