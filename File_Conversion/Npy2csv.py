import numpy as np
import pandas as pd
import os 

npy_path="NPY_files"                  #.mat folder location 
csv_path=npy_path+"_CSV\\"

os.makedirs(csv_path,exist_ok=True)

npyfile=[]
for file in os.listdir(npy_path):
    if file.endswith('.npy'):                   #Only .mat files
        npyfile.append(file)    
print(npyfile)

for i in npyfile:
    x=np.load(npy_path+"\\"+i)
    df=pd.DataFrame(x)
    df.to_csv(csv_path+i.replace(".npy","")+".csv")

print("Done")
