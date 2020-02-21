#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:35:25 2019

@author: neelu
"""

import csv

#with open('history.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    
##    next(csv_reader)            # to skip the first line
#    for line in csv_reader:
#        print(line[4])
#        
with open('history.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(csv_reader)
#    next(csv_reader)            # to skip the first line
#    for line in csv_reader:
#        #print(line)
#        print(line['    "rms[RhoV]"   '])
        
    with open('new_write.csv','w') as new_file:
        fieldnames = ['    "rms[RhoU]"   ','    "rms[RhoV]"   ','    "rms[RhoW]"   ','    "rms[RhoE]"   ', '    "rms[Rho]"    ', '     "rms[nu]"    ', 'Inner_Iter','Outer_Iter', 'Time_Iter']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)#, #delimiter=',')
#        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['Outer_Iter']
            del line['Time_Iter']
            csv_writer.writerow(line)