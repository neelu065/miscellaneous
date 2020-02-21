import subprocess as sp
import shlex
import os


for i in range(1,10):
    os.makedirs(os.path.join('/home/neelu/Desktop/Template_glyph/DESIGN', 'Gen_' + str(i)))

    print(os.system('pwd'))
