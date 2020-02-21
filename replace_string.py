#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:39:19 2020

@author: neelappagouda
"""

#str_old = '  $_TMP(mode_1) initialize -strict -type {PLOT3D} {/home/neelu/Desktop/createFFD/Test_wing_3D/input_files/wing_important/wing_temp.x}'
#str_new = 'Hi'
#with open('wing_import.glf','r') as f:
#    with open('wing_edit', 'w') as g:
#        
#        for line in f:
#            line.replace('wing_temp', 'pointwise')
#            g.write(line)
#


import fileinput
i = 5
# Does a list of files, and
# redirects STDOUT to the file in question
for line in fileinput.input('wing_edit', inplace = 1): 
    print(line.replace("pointwise_wing_{}.format(i)", "pointwise_wing_{}".format(i)).rstrip())