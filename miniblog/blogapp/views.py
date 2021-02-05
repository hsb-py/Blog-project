from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from blogapp.forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')    

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts}) 
    else:
        return redirect("/login/")    

def user_logout(request):
    logout(request)
    return redirect('/') 

def user_signup(request):
    form=SignUpForm()
    if request.method=="post":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!! You have become an Author')
            form.save()
        else:    
            form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})  

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname= form.cleaned_data["username"]
                upass= form.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not none:
                    login(request,user)
                    messages.success(request,'Logged in Successfully !!!')
                    return redirect('/dashboard/')
        else:            
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})              
    else:
        return redirect('/dashboard/')