from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import tweepy#twitter app
import numpy as np
import pandas as pd
from django.contrib import messages
from sklearn import svm
from sklearn.metrics import classification_report, accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split
from joblib import dump ,load #write in binary format, read in binary fromat
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob#processing textual data
from nltk.corpus import stopwords
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import pickle
import nltk
from logReg.forms import login_data
from django.conf import settings
nltk.download('stopwords')#English words
stop = stopwords.words('english')
from logReg.models import user

from logReg.models import encr_data
from logReg.models import post_data
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt,csrf_protect
def index(request):
    return render(request, 'index.html')
def home_page(request):
    return render(request,'test.html')
def thankyou(request):
    return render(request,'success.html')
def exit(request):
    return render(request,'index.html')
def userreg(request):
    if request.method=='POST':
        fname=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        mobile=request.POST['mobile']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user(fname=fname,gender=gender,age=age,mobile=mobile,email=email,username=username,password=password).save()
        messages.success(request,'The New user' + request.POST['name'] + 'is saved successfully')
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')  
'''
def login(request):
    if request.method=="POST":
        fm=login_data(request.POST)
        if fm.is_valid():
            print('form validated')
            name=fm.cleaned_data['name']
            password=fm.cleaned_data['password']
            print('Name',name)
            print('password:',password)
            return render(request,'Master.html',{'nm':name})
    else:    
        fm = login_data()
    return render(request,'login.html',{'form':fm})
    
def home(request):
    if request.method=="POST":
        content = request.POST.get('content', '')
        if content:
            print('Content:', content)   
            return HttpResponseRedirect('/success/')    
    return render(request,'home.html')'''
def recent(request):
    stud = post_data.objects.all()
    print("Myoutput",stud)
    return render(request,'recent.html',{'stu': stud})
def test(request):
    if request.method=="POST":
        content = request.POST.get('content', '')
        if content:
            print('Content:', content)  
            content=[content]
            predictor = load("data/SVM_MODEL.joblib")
            vec = open('data/vectorizer.pickle', 'rb')
            tf_vect = pickle.load(vec)
            X_test_tf = tf_vect.transform(content)
            y_predict = predictor.predict(X_test_tf)
            print(y_predict[0])
            if y_predict[0]==0:
                print("Normal Sentence")
                messages.success(request,'The Tweet is Normal'+ request.POST['content'])
                print("Content:",content)
                def listToString(s): 
                    str1 = ""  
                    for ele in s: 
                        str1 += ele  
                    return str1 
 
                content=listToString(content)
                bad_chars = ['[', ',', ']']
                for i in bad_chars :
                    con = content.replace(i, '')
                abc=str(con)
                auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
                auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
                api = tweepy.API(auth)
                api.update_status(con)
                from cryptography.fernet import Fernet#encry and decrypt data
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encMessage = fernet.encrypt(abc.encode())
                print("original string: ", abc)
                print("encrypted string: ", encMessage)
                post_data(data=abc).save()
        
                
                decMessage = fernet.decrypt(encMessage).decode()
                print("decrypted string: ", decMessage)
                encr_data(data=encMessage).save()
                A =" The Tweet is Not Vulger,You want to post it on Twiiter?"
                messages.info(request, abc + A )
                return HttpResponseRedirect('/success/',messages)
            else:
                print("Sarcastic Sentence")
                messages.success(request,'The Tweet is Sarcastic'+ request.POST['content'])
                A =" The Tweet is Vulger"
                messages.info(request, A)
                #messages.error(request,'The Tweet is Vulger')
                return HttpResponseRedirect('/success/',messages)

            
            

    
    return render(request,'test.html')   
def sample(request):
    return render(request,'sample.html')
def show(request):
    if request.method=="POST":
        fm=login_data(request.POST)
        if fm.is_valid():
            print('form validated')
            name=fm.cleaned_data['name']
            password=fm.cleaned_data['password']
            print('Name',name)
            print('password:',password)
            request.session['name']=name
            return HttpResponseRedirect('/sample/')
            return render(request,'success.html',{'nm':name})
    else:    
        fm = login_data()
    return render(request,'reg.html',{'form':fm})

def logout(request):
    try:
        del request.session['name']
    except:
        return render(request,'index.html')
    return render(request,'index.html')
def sub(request):
	if request.method == 'POST':
		content = request.POST.get('content', '')

		if content:
			print('Content:', content)

			auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
			auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

			api = tweepy.API(auth)
			api.update_status(content)

			return redirect('index')
	return render(request, 'sample.html')

'''
def test(request):
    if request.method=="POST":
        
        content = request.POST.get('content', '')
        if content:
            print('Content:', content)

        
            content=[content]
            predictor = load("hello/data/SVM_MODEL.joblib")
            vec = open('hello/data/vectorizer.pickle', 'rb')
            tf_vect = pickle.load(vec)
            X_test_tf = tf_vect.transform(content)
            y_predict = predictor.predict(X_test_tf)
            print(y_predict[0])
            if y_predict[0]==0:
                print("Normal Sentence")
                messages.success(request,'The Tweet is Normal'+ request.POST['content'])
                print("Content:",content)
                abc=str(content)
                from cryptography.fernet import Fernet
                message = "hello geeks"
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encMessage = fernet.encrypt(abc.encode())
                print("original string: ", abc)
                print("encrypted string: ", encMessage)
                decMessage = fernet.decrypt(encMessage).decode()
                print("decrypted string: ", decMessage)
                return render(request,'index.html')
            else:
                print("Sarcastic Sentence")
                messages.success(request,'The Tweet is Sarcastic'+ request.POST['content'])
                return render(request,'index.html')
              
    return render(request, 'Master.html')'''
