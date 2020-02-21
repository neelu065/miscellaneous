

import csv

wing_number = 3
wing_sections = 4

with open('of_func.csv','r') as f:
    csv_reader = csv.DictReader(f)

    with open('Chord_values.csv','w') as new_file:
         fieldnames = ['WING','Sec_1','Sec_2','Sec_3','Sec_4','Sec_5']
         csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames , delimiter='\t')
         csv_writer.writeheader()


         for line in csv_reader:
             new_file.write('{}'.format(wing_number))
             new_file.write('\t\t\t')
             for i in range(wing_sections):

                new_file.write(line['STATION{}_THICKNESS'.format( i+1 )])
                new_file.write('\t')
                # csv_writer.writerow(line['STATION{}_CHORD'.format( i+1 )])
