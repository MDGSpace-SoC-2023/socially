from .models import Post, Blog, LoginUser, RegisterUser, UserPost, UserJokes, Memes
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields="__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = "__all__"

class  UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = "__all__"



class UserJokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJokes
        fields = "__all__"


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memes
        fields = "__all__"
        