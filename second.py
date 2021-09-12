import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import string
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

url = r"C:\Users\mehak\Desktop\thb data.csv"
names=['specialty', 'symptoms','number']
df=pd.read_csv(url,names=names)
specialties={}
count=0
max=0


df["symptoms 2.0"] = df["symptoms"].str.replace('[^a-zA-Z\']', ' ')
    
    #Remove Unicode characters
df["symptoms 2.0"] = df["symptoms 2.0"].str.replace('[^\x00-\x7F]+', '')
df["symptoms 2.0"] = df["symptoms 2.0"].str.replace(',', '')
    
    #Convert to lowercase to maintain consistency
df["symptoms 2.0"] = df["symptoms 2.0"].str.lower()

symptoms_list=[]
for i in range(len(df['symptoms 2.0'])):
    symptoms=df['symptoms 2.0'][i].split()
    for i in range(len(symptoms)):
        if symptoms[i] not in symptoms_list:
            symptoms_list.append(symptoms[i])
specs=df.groupby('specialty')
spec_list=["symptoms"]
for s in specs:
    
    spec_list.append(s[0])
    
new_df=pd.DataFrame([[symptoms_list[0],"","","","","","","","","","","","","","","","","","","","","","","","",""]],columns=spec_list)
for i in range(len(symptoms_list)-1):
    data=pd.DataFrame([[symptoms_list[i+1],"","","","","","","","","","","","","","","","","","","","","","","","",""]],columns=spec_list)
    new_df=new_df.append([data],ignore_index=False)
    
