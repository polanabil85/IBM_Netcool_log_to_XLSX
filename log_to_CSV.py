import pandas as pd 
import numpy as np
nan = np.nan
rows=[]
dict1={}
with open('samplelog.log','r') as reader:
    for line in reader:
        if 'Event Processor' in line:
            if '[Event Processor] Processing alert' in line:
                continue
            strin1 = line.split(']')
            strin2 = strin1[1].split(':')
            dict1[strin2[0].strip()]=' '.join(strin2[1:]).strip()
        if 'Processing Alert...' in line:
            rows.append(dict1)
            dict1={}
datafr=pd.DataFrame.from_dict(rows, orient='columns')
datafr.to_excel('alarms.xlsx')
