import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


url = r"C:\Users\mehak\Desktop\thb data.csv"
names=['specialty', 'symptoms','number']
df=pd.read_csv(url,names=names)

df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.7


df["symptoms 2.0"] = df["symptoms"].str.replace('[^a-zA-Z\']', ' ')
    
    #Remove Unicode characters
df["symptoms 2.0"] = df["symptoms 2.0"].str.replace('[^\x00-\x7F]+', '')
df["symptoms 2.0"] = df["symptoms 2.0"].str.replace(',', '')
    
    #Convert to lowercase to maintain consistency
df["symptoms 2.0"] = df["symptoms 2.0"].str.lower()

X = pd.DataFrame(df.iloc[:, :1].values)
y = pd.DataFrame(df.iloc[:, 1].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print(X_train)


model = DecisionTreeClassifier()
vectorizer = CountVectorizer()
X_train=vectorizer.fit_transform(X_train[0])
#how to use counts to add weight to words

# fit the model with the training data
model.fit(X_train,y_train)

predict_train = model.predict(X_train)
accuracy_train = accuracy_score(y_train,predict_train)
print('accuracy_score on train dataset : ', accuracy_train)
predict_test = model.predict(X_test)
accuracy_test = accuracy_score(y_train,predict_test)
print('accuracy_score on test dataset : ', accuracy_test)
