import pandas as pd 
import seaborn as sns   
import matplotlib.pyplot as plt 
import os
df = pd.read_csv(r"C:\Users\HP\Downloads\spotify-2023.csv", encoding='latin1')  # Importing data 
print(df.head()) 
print(df.columns)

df.isnull().sum()  #Data Cleaning 
df.dropna(inplace=True) 

df['artist(s)_name'].value_counts().head()  # Data Analysis

import numpy as np

plt.figure(figsize=(10,5))

sns.histplot(np.log10(pd.to_numeric(df['streams'], errors='coerce') + 1), bins=50)

plt.title("Log Distribution of Streams")
plt.xlabel("Log(Streams)")
plt.ylabel("Count")

plt.savefig("graph.png")
plt.close()

print("Saved as:",os.getcwd())  #visulaization of data


 





            
