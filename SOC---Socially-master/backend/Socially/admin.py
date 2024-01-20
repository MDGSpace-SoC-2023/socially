from django.contrib import admin
from .models import RegisterUser,LoginUser,Blog,Post, UserPost,  UserJokes, Memes
# Register your models here.
admin.site.register(RegisterUser)
admin.site.register(LoginUser)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(UserPost)
admin.site.register(Memes)
admin.site.register(UserJokes)