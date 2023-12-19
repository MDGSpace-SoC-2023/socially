from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from django.shortcuts import redirect
from django.utils import timezone


# Create your views here.
def display(request):
    return render(request,"login_or_register.html",{})

def register_page(request):
    
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
    
   


    