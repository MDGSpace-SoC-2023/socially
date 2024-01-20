from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    username = forms.CharField()
    email = forms.EmailField()

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = Userfields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']