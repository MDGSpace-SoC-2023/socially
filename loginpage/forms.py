from django import forms 
from .models import RegisterUser,LoginUser,Blog,Post

class RegisterForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = RegisterUser
        
        fields = ('username','password','image_url')

class LoginForm(forms.ModelForm):
    class Meta:
        model=RegisterUser
        fields = ('username','password')
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('type','title','content')

