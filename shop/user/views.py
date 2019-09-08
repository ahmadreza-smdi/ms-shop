from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from .models import Customer,Purchase
from django.contrib.auth.models import User
import threading
from django.contrib.auth.decorators import login_required
from log_package import logg
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

global site_visitor
def logged_in(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def main(request):
    if request.method == 'GET':
        pass
    return render(request,'index.html')

def loginn(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        print("password",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("login is true")
            logg.loging(username,request,'login')
            return HttpResponseRedirect('/dashboard')
        else:
            print("login is false")
            return HttpResponseRedirect('/login/')

    return render(request,'Signin.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            logg.loging(username,request,'register')
        else:
            for msg in form.error_messages:
                print(form.error_message[msg])

        return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request,'Signup.html',{'form':form})

@login_required
def dashboard(request):
    # if request.user.is_authenticated():
    #     username = request.user.username
    return render(request,'dashboard.html',{"user_name":request.user.username})
    # else:
    #     return HttpResponseRedirect('/login/')
@login_required
def settings(request):
    username = request.user.get_username()
    p = Customer.objects.get(user__username = username)
    print(p.phone_number)
    if request.method == 'POST':
        username = request.user.username
        national_code=request.POST.get('national_code')
        Age=request.POST.get('Age')
        phone_number=request.POST.get('phone_number')
        Sex=request.POST.get('Sex')
        address=request.POST.get('address')
        birthdate=request.POST.get('birthdate')
        a = Customer.objects.filter(user__username=username).update(phone_number =phone_number,sex = Sex,age = Age, national_code = national_code ,address = address )
        if a:
            logg.loging(username,request,'Settings has updated')
        return HttpResponseRedirect('/dashboard')
    if request.method == 'GET':
        return render(request,'settings.html',{'p':p})
    else:
        return HttpResponseRedirect('/login/')


def logout_view(request):
    username = request.user.username
    logout(request)
    logg.loging(username,request,'logout')
    return HttpResponseRedirect('/login/')
