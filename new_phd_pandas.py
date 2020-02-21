#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:13:42 2019

@author: neelu
"""
import pandas as pd

print('make sure that your input file name is plot_in.csv')


print('Importing .csv file...')
df = pd.read_csv('plot_in.csv')

print('reading of csv file is completed...')
df.drop(df.head(10).index, inplace=True)



print('Processing...')
N = 3
""" this value represent the column value which need
   to be plot (1 = x velocity, 2 = y velocity , so on) """

with open('plot_out.csv','w') as new_file:

    for row in range(len(df)):
        asd = df.iat[row,0].split()

        time = (asd[0])
        velocity = (asd[N].replace(")", " "))

        new_file.write('{} \t {} \n'.format(time,velocity))

print('file created')

print('Output file is saved as plot_out.csv')
