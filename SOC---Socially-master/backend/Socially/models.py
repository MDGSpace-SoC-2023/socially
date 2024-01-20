from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
# Create your models here.
class RegisterUser(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null= True, blank = True )
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    image_url = models.ImageField(blank=True)
    
    def __str__(self):
        return self.username
    def upload(self):
        self.published_date= timezone.now()
        self.save()
        
class LoginUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
        
    def __str__(self):
        return self.username
        
class Sample(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
        
    def __str__(self):
        return self.username
        
class Blog(models.Model):

    type  = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True,null = True, default=timezone.now())

    
    
class Post(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.CharField(max_length = 200)
    likes = models.IntegerField()
    

class UserPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=40)
    comments = models.JSONField( encoder=None, decoder=None)
    likes = models.IntegerField()
    caption = models.CharField(max_length=300)
    format = models.CharField(max_length=50, null=True, blank = True)


    
class UserJokes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=40)
    setup = models.CharField(max_length=100, null=True, blank = True)
    delivery = models.CharField(max_length= 100, null=True, blank = True)
    joke = models.CharField(max_length = 100, null=True, blank=True) 


class Memes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)



    
    