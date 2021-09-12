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
filename = 'chatbot_model_4.sav'
loaded_model = pickle.load(open(filename, 'rb'))
probabilty= pd.DataFrame(loaded_model.predict_proba(['ear']), columns=loaded_model.classes_)
probability_score=probabilty.melt()