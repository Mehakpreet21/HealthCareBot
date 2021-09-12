import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import string
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pickle
from sklearn.metrics import classification_report

url = r"C:\Users\mehak\Desktop\thb data.csv"
names=['specialty', 'symptoms','number']
dataset=pd.read_csv(url,names=names)

specialties={}
count=0
max=0

dataset["symptoms"] = dataset["symptoms"].str.replace('[^a-zA-Z\']', ' ')
    
    #Remove Unicode characters
dataset["symptoms"] = dataset["symptoms"].str.replace('[^\x00-\x7F]+', '')
dataset["symptoms"] = dataset["symptoms"].str.replace(',', '')
    
    #Convert to lowercase to maintain consistency
dataset["symptoms"] = dataset["symptoms"].str.lower()

for i in range(len(dataset['specialty'])):
    if dataset["specialty"][i]=="PAEDIATRICS" or dataset["specialty"][i]=="GENERAL PRACTICE":
        dataset.drop([i], axis=0, inplace=True)  
s=dataset.groupby("specialty").indices
df = pd.DataFrame(columns=['specialty','symptoms','number'])
specialties=[]

for specialty in s:
    specialties.append(specialty)
for i in specialties:
    if len(s[i])<2241:
        length=len(s[i])
        dataset_new=dataset.iloc[s[i][0]:s[i][-1], :]
     
    df=df.append([dataset_new]*round(2241/length), ignore_index=False)
#change 1166

'''for i in range(0,dataset.shape[0]):
    if dataset['specialty'][i]=="PULMONOLOGY":
        dataset_p=dataset.iloc[i:i+1, :]'''

dataset=dataset.append([df], ignore_index=False)
#subsets

'''
for i in range(0,dataset.shape[0]):
    if dataset['specialty'][i] not in specialties:
        specialties[dataset['specialty'][i]]=1
    else:
        specialties[dataset['specialty'][i]]+=1
for i in range(dataset.shape[0]):
    if dataset['specialty'][i]=="HOMEOPATHY":
        print(dataset["specialty"][i])
'''

def text_process(symptom):
    nonpunc=[char for char in symptom if char not in string.punctuation]
    nonpunc = "".join(nonpunc)
    return [word for word in nonpunc.split() if word.lower() not in stopwords.words('english')]


transformer=CountVectorizer(analyzer=text_process)
t=transformer.fit(dataset['symptoms'])

count=0
max=0
ind=[]

symps_train, symps_test, y_train, y_test = train_test_split(
   np.array(dataset['symptoms']), np.array(dataset['specialty']), test_size=0.01)
#remove gen practice and paediatrics
classifier = SVC(C=150, gamma=2e-2, probability=True)
#create another model w 0 test size.

pipeline=Pipeline([
        ('vect',CountVectorizer()),
        ('tfidf',TfidfTransformer()),
        ('clf',classifier)
    ])
'''
clf=SVC(probablity=True)
probs = clf.predict_proba(symps_test)
best_n = np.argsort(-probs, axis=1)[:, :2]
'''
#n largest
#dataframe of the outputs
#transform the probabilities 
#embed the array in a dataframe

#sav file
#how to save a ml model

pipeline.fit(symps_train,y_train)
probabilty= pd.DataFrame(pipeline.predict_proba(["leg pain"]), columns=pipeline.classes_)
probability_score=probabilty.melt()
probability_score.nlargest(3,'value')['variable']
#wont use preds
predictions=pipeline.predict(symps_test)
print(classification_report(y_test, predictions))

ind=[]
for i in range(dataset.shape[0]):
    ind.append(i)
dataset['index']=ind
dataset.set_index('index',inplace=True)
'''
symptoms_list=[]
for i in range(len(df['symptoms 2.0'])):
    symptoms=dataset['symptoms 2.0'][i].split()
    for i in range(len(symptoms)):
        if symptoms[i] not in symptoms_list:
            symptoms_list.append(symptoms[i])
specs=df.groupby('specialty')
spec_list=["symptoms"]
for s in specs:
    
    spec_list.append(s[0])

new_df=pd.DataFrame(columns=spec_list)
for i in range(len(symptoms_list)-1):
    probabilty= pd.DataFrame(pipeline.predict_proba([symptoms_list[i]]), columns=pipeline.classes_)
    data=pd.DataFrame([[symptoms_list[i],probabilty[new_df.columns[1]][0],probabilty[new_df.columns[2]][0],probabilty[new_df.columns[3]][0],probabilty[new_df.columns[4]][0],probabilty[new_df.columns[5]][0],probabilty[new_df.columns[6]][0],probabilty[new_df.columns[7]][0],probabilty[new_df.columns[8]][0],probabilty[new_df.columns[9]][0],probabilty[new_df.columns[10]][0],probabilty[new_df.columns[11]][0],probabilty[new_df.columns[12]][0],probabilty[new_df.columns[13]][0],probabilty[new_df.columns[14]][0],probabilty[new_df.columns[15]][0],probabilty[new_df.columns[16]][0],probabilty[new_df.columns[17]][0],probabilty[new_df.columns[18]][0],probabilty[new_df.columns[19]][0],probabilty[new_df.columns[20]][0],probabilty[new_df.columns[21]][0],probabilty[new_df.columns[22]][0]]],columns=spec_list)
    new_df=new_df.append([data],ignore_index=False)
new_ind=[]
for i in range(new_df.shape[0]):
    new_ind.append(i)
new_df['index']=new_ind
new_df.set_index('index',inplace=True)

new_df["number"]=dataset['number']
new_df.set_index('symptoms')
'''

if __name__ == '__main__':   
    filename = 'chatbot_model_4.sav'
    pickle.dump(pipeline, open(filename, 'wb'))