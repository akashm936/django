
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

def Home(request):
    return render(request,'home.html')

def Doctor(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
 
        
        if password != cpassword:
            messages.error(request,'password can not match')
            return redirect('/doctor')
        
        else:
            User = User.object.create(username = uname,email = email, password = cpassword)
            User.first_name = fname
            User.last_name = lname
            User.save()
            messages.success(request,'your account successfully created')
            return redirect('/login')
            
            
    return render(request,'doctor.html')

def patient(request):
    return render(request,'patient.html')

def login(request):
    return render(request,'login.html')


