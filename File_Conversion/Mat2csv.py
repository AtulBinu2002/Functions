from scipy.io import loadmat
import pandas as pd
import os

mat_path="E:\FYI\File_002"                  #.mat folder location 
csv_path=mat_path+"_CSV\\"                  #.csv location to save

os.makedirs(csv_path,exist_ok=True)

matfile=[]
for file in os.listdir(mat_path):
    if file.endswith('.mat'):                   #Only .mat files
        matfile.append(file)    
print(matfile)

for i in matfile:
    data=loadmat(mat_path+"\\"+i)
    x=data["data_mat"]
    df=pd.DataFrame(x)
    df.to_csv(csv_path+i.replace(".mat","")+".csv",index=False)
