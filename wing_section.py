import numpy as np
import pandas as pd
with open('template.cfg','r') as file:

    for line in file:
        if line.startswith('GEO_LOCATION_STATIONS'):
            ab=line.split(' ')
            a = pd.DataFrame(ab)
            print(a)
            print(a.iat[1,0].split())
            # ab = np.asarray(line)
    # print(len(ab))
