import pandas as pd
import os, glob
from datetime import datetime

CURRENT_DIR = os.getcwd()

list = os.path.join(CURRENT_DIR,'BOM_list.xlsx')
df = pd.read_excel(list)
print(df)

for i in df['MLFB'].index:
    MLFB = df.loc[i, 'MLFB']
    print(MLFB)

