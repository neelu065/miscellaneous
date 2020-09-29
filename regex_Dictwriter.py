#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:14:54 2020

@author: neelappagouda
"""


import re
import operator
import csv
import sys

filename = sys.argv[1]
number_of_error_messages = {}
number_of_enteries_per_user = {}

with open(filename,'r') as sys_file:
    for line in sys_file.readlines():
        if re.search(r"ERROR:", line):
            error = re.search(r"(ERROR:) (.*) \((\w*)\)$", line)
            if error[2] not in number_of_error_messages:
                number_of_error_messages[error[2]] = 0
            number_of_error_messages[error[2]] += 1
            
            if error[3] not in number_of_enteries_per_user:
                number_of_enteries_per_user[error[3]] = [0, 0]
            number_of_enteries_per_user[error[3]][1] += 1
            
        if re.search(r"INFO:", line):
            info = re.search(r"(INFO:) (.*) \((\w*)\)$", line)
            if info[3] not in number_of_enteries_per_user:
                number_of_enteries_per_user[info[3]] = [0, 0]
            number_of_enteries_per_user[info[3]][0] += 1

number_of_error_messages = dict(sorted(number_of_error_messages.items(), key = operator.itemgetter(1), reverse=True))
number_of_enteries_per_user = dict(sorted(number_of_enteries_per_user.items(), key = operator.itemgetter(0)))

with open('error_message.csv','w') as f:
    csv_writer = csv.DictWriter(f, fieldnames = ['Error', 'Count'])
    csv_writer.writeheader()
    for key in number_of_error_messages:
        f.write('{}, {}\n'.format(key, number_of_error_messages[key]))
    
with open('user_statistics.csv','w') as g:
    csv_writer = csv.DictWriter(g, fieldnames = ['Username', 'INFO', 'ERROR'])
    csv_writer.writeheader()
    for key in number_of_enteries_per_user:
        g.write('{}, {}, {}\n'.format(key, number_of_enteries_per_user[key][0], number_of_enteries_per_user[key][1]))

        
            
            
            
                
                








