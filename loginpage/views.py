from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm,BlogForm,LoginForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from . import forms 

from .models import RegisterUser,Sample,Blog,Post


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

def blog_list(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"blog_list.html",{'blogs':blogs})
    
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})
def blog_edit(request):
    form = forms.BlogForm()
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            print("Validation complete! ")
            type = form.cleaned_data['type']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user_input = Blog(type=type,content = content, title= title, published_date = timezone.now())
            user_input.save()
            return redirect('literature')
        else:
            form = BlogForm()
    return render(request,"blog_edit.html",{'form':form})
        



    