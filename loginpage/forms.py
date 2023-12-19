from django import forms 
from .models import RegisterUser,LoginUser

class RegisterForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = RegisterUser
        
        fields = ('username','password','image_url')

class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginUser
        fields = {'username','password'}

