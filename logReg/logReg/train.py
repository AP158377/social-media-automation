
import pandas as pd, numpy as np, re

from sklearn.metrics import classification_report, accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split
import tkinter as tk
from sklearn import svm
from PIL import Image, ImageTk
from joblib import dump , load
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob#processing textual data
from nltk.corpus import stopwords
from sklearn import metrics
from sklearn.model_selection import GridSearchCV#set of parameters in a grid
import pickle
import nltk#natural language
#######################################################################################################
nltk.download('stopwords')
stop = stopwords.words('english')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')#tagging accuracy
result = pd.read_csv(r"D:\social media automation\logReg\data\sarcasm_dataset.csv",encoding = 'unicode_escape')

result.head()#get the first n rows.
       
result['headline_without_stopwords'] = result['headline'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
###########################################################################################################################################
   
def pos(review_without_stopwords):
    return TextBlob(review_without_stopwords).tags
   
   
os = result.headline_without_stopwords.apply(pos)
os1 = pd.DataFrame(os)
   #
os1.head()
   
os1['pos'] = os1['headline_without_stopwords'].map(lambda x: " ".join(["/".join(x) for x in x]))
   
result = result = pd.merge(result, os1, right_index=True, left_index=True)
result.head()
result['pos']
review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['is_sarcastic'],
                                                                             test_size=0.2, random_state=13)
   
tf_vect = TfidfVectorizer(lowercase=True, use_idf=True, smooth_idf=True, sublinear_tf=False)
   
X_train_tf = tf_vect.fit_transform(review_train)
X_test_tf = tf_vect.transform(review_test)
   
   ###########################################################################################################################
def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01, 0.1, 1, 10]
    gammas = [0.001, 0.01, 0.1, 1]
    param_grid = {'C': Cs, 'gamma': gammas}
    grid_search = GridSearchCV(svm.SVC(kernel='linear'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    return grid_search.best_params_
   
   
svc_param_selection(X_train_tf, label_train, 5)
   #
   
clf = svm.SVC(C=10, gamma=0.001, kernel='linear')   
clf.fit(X_train_tf, label_train)
pred = clf.predict(X_test_tf)
   
with open('vectorizer.pickle', 'wb') as fin:
       pickle.dump(tf_vect, fin)
with open('mlmodel.pickle', 'wb') as f:
       pickle.dump(clf, f)
   
pkl = open('mlmodel.pickle', 'rb')
clf = pickle.load(pkl)
vec = open('vectorizer.pickle', 'rb')
tf_vect = pickle.load(vec)
   
X_test_tf = tf_vect.transform(review_test)
pred = clf.predict(X_test_tf)
   
print(metrics.accuracy_score(label_test, pred))
   
print(confusion_matrix(label_test, pred))
   
print(classification_report(label_test, pred))

      
print("=" * 40)
print("==========")
print("Classification Report : ",(classification_report(label_test, pred)))
print("Accuracy : ",accuracy_score(label_test, pred)*100)
accuracy = accuracy_score(label_test, pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
ACC = (accuracy_score(label_test, pred) * 100)
repo = (classification_report(label_test, pred))
   
   
dump (clf,"SVM_MODEL.joblib")#write data into file
print("Model saved as SVM_MODEL.joblib")
   