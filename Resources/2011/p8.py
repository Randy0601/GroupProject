import glob   
import pandas as pd   
import os   
import sys   
path = '/Users/ghassan/project-1/GroupProject/Resources/2011/*.xls'
files=glob.glob(path)
print(files)
for fIn in files:
   try:
      with open(fIn, 'r') as f:
          df = pd.read_excel(fIn,encoding='latin_1',sheet_name=0)
          df.columns = df.columns.str.strip()
          outfile=fIn+'.csv'
      with open(outfile, 'w') as fileout:
          df.to_csv(fileout,sep="|",index=False)
   except IOError as e:
      print("I/O error({0}): {1}".format(e.errno, e.strerror))
print("done")
