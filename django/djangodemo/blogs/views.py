from email import message
from django.shortcuts import render,redirect
from .models import Post 
from django.contrib.auth.models import User,auth
from django.contrib import messages
  

# Create your views here.

def hello(request):
    
    return render(request,'index.html')

def page1(request):
    #query ข้อมูลมาจาก model
    data=Post.objects.all()
    return render(request,'page1.html',{'posts':data})

def createForm(request):

    return render(request,'Form.html')

def addBlogs(request):
   
    return render(request,'result.html')

def registerForm(request):
 

    return render(request,'registerForm.html')

def addRegis(request):
    username =request.POST['username']
    fname =request.POST['fname']
    lname =request.POST['lname']
    email =request.POST['email']
    password =request.POST['password']
    repassword =request.POST['repassword']
   
   
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'usernameนี้มีคนใช้แล้ว')
            return redirect('/registerForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Emailนี้มีคนใช้แล้ว')
            return redirect('/registerForm')
        else :
            user=User.objects.create_user(
            username=username,
            first_name=fname,
            last_name=lname,
            email=email,
            password=password
            )
            user.save()
            return redirect('/page1')
    else :
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/registerForm')

def loginForm(request):
    
    return render(request,'loginForm.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
   
   #login เช็ค username กับ password ตรงกันในฐานข้อมูลไหม
    
    user=auth.authenticate(username=username,password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('/page1')
    else:
        msg=messages.info(request,"ไม่พบข้อมูล")
        return redirect('/loginForm')
        
def logout(request):
    auth.logout(request)
    return redirect('/page1')
    