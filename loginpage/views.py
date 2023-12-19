from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from . import forms 

from .models import RegisterUser,Sample


# Create your views here.
def display(request):
    return render(request,"login_or_register.html",{})

def register_page(request):
    form = forms.RegisterForm()
    
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            me = User.objects.get(username='Aaryan')
            print("Validation complete")
            username1 = form.cleaned_data['username']
            password1 =  form.cleaned_data['password']
            image_url1 = form.cleaned_data['image_url']
            user_input = RegisterUser(username=username1,password= password1, image_url = image_url1,published_date = timezone.now(),user = me)
            user_input.save()
            return render(request,'welcome.html',{})
    return render(request,'registerpage.html',{'form':form})
    
    

def login_page(request):
    form = forms.LoginForm()
    
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("Validation complete")
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            all_entries = RegisterUser.objects.all()
            print(all_entries)
            q1 = RegisterUser.objects.filter(username__startswith=username)
            q2 = q1.filter(password__startswith=password)
            if(q2):
                return render(request,'welcome.html',{})
            else:
                return render(request,'failed.html',{})
            
    return render(request,'loginpage.html',{'form':form})
    
   


    