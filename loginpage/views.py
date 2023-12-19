from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from django.shortcuts import redirect
from django.utils import timezone
from . import forms 


# Create your views here.
def display(request):
    return render(request,"login_or_register.html",{})

def register_page(request):
    form = forms.RegisterForm()
    
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("Validation complete")
            print("Username: "+ form.cleaned_data['username'])
            print("Password: "+ form.cleaned_data['password'])
            #print("IMG URL: " +form.cleaned_data['image_url'])
            return render(request,'welcome.html',{})
    return render(request,'registerpage.html',{'form':form})
    
    

def login_page(request):
    print("hello")
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Name" + form.cleaned_data['username'])
            print("hey")
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('welcome.html')
        else:
            form = RegisterForm()
        return redirect ('failed.html')
    
   


    