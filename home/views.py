from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import User
from django.contrib.auth.models import User
#from .forms import Signup, Verify 
from django.contrib import messages

#For Message API
import requests
import json
import random

#SMS_API
#Apikey:- WCGEJ8F2H0SYHJYTCBMJW3PQLEEX2FQP
#secretkey:- F08ZS2RZXXAB62KB
randnum = random.randint(1000,9999)
URL = 'https://www.sms4india.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
# get response
#msg = f'your OTP is {randnum}'
#response = sendPostRequest(URL, 'WCGEJ8F2H0SYHJYTCBMJW3PQLEEX2FQP', 'F08ZS2RZXXAB62KB', 'stage', '8209137041', 'modikartik19@gmail.com', msg)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
# print(response.text)'''

def Signup(request):
    form = Signup()
    #messages.success(request, 'You !!')
    return render(request,"/index.html")

class Aftersign(View):
    def get(self,request):
        error = "Invalid method"
        form = Signup()
        return render(request,"users/signup.html",{'f':form,'error':error})
    
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            data = {
            'username' : form.cleaned_data['username'],
            'email' : form.cleaned_data['email'],
            'password' : form.cleaned_data['password'],
            'pic' : form.cleaned_data['pic']
            }
            try:
                obj = Adduser.objects.get(email=data['email'])
            except Exception:   
                new_obj = Adduser.objects.create(**data)
                new_obj.save()
                form = Login()
                return render(request,"users/login.html",{'f':form})
            else:
                error = "User already exists...."
                form = Signup()
                return render(request,"users/signup.html",{'f':form,'error':error})
        else:
            error = "Invalid form...."
            form = Signup()
            return render(request,"users/signup.html",{'f':form,'error':error})

# Create your views here.
#Homepage
def home(request):
    '''context ={
        "variable":"This is sent"
    }'''
    return render(request,'index.html')
    #return HttpResponse("This is Home page")
    
    
'''
def login(request):
    if request.session.get('mobile'):
        #return HttpResponse("""
                #<a href='/users/logout/'>LOGOUT</a>""")
        return render(request,"users/login1.html")
    else:
        form = Login()
        return render(request,"users/login.html",{'f':form})

def afterlogin(request):
    form = Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            obj = User.objects.get(mobile=mobile)
        except:
            error = "No such user...."
            form = Login()
            return render(request,"users/login.html",{'f':form,'error':error})
        else:
            if password == obj.password:
                request.session['email'] = email
                #return HttpResponse("""Email : {} and password {}
                #<a href='/users/logout/'>LOGOUT</a>""".format(email,password))
                return render(request,"users/login1.html")
            else:
                error = "Invalid password"
                form = Login()
                return render(request,"users/login.html",{'f':form,'error':error})
    else:
        error = "Invalid form..."
        return render(request,"users/login.html",{'error':error})

      
#Signup



#Shop
def shop(request):
    return render(request,'shop-grid.html') 

#contact
def contact(request):
    return render(request,'contact.html')

#Login
def login(request):
  return render(request,'login.html')  
    

def test(request):
    return render(request,'test.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone  = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message successfully sent!!')

    return render(request,'contact.html')'''
