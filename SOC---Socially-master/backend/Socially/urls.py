from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path("",views.display,name="display"),
    # path("register/",views.register_page,name="register"),
    # path("login/",views.login_page,name="login"),
    # path("literature/",views.blog_list, name="literature"),
    # path("blogs/<int:pk>/",views.blog_detail, name = "blog_detail"),
    # path("blogs/new/",views.blog_edit, name ="blog_edit"),
    path("blogpage/",views.UserBlogsView.as_view()),
    path("newblog/", views.UserBlogView.as_view()),
    path("blog/<int:id>/", views.UserBlogView.as_view()),
    path("post/",views.UserPostsView.as_view()),
    path("newpost/", views.UserPostView.as_view()),
    path("post/<int:id>/", views.UserPostView.as_view()),
    path('api/login/', views.api_login, name='api-login'),
    path('api/logout/', views.api_logout, name='api-logout'),
    path('api/user-details/',views.api_user_details, name='api-user-details'),
    path("jokes/",views.UserJokesView.as_view()),
    path("newjoke/", views.UserJokeView.as_view()),
    path("joke/<int:id>/", views.UserJokeView.as_view()),
    path("memes/",views.UserMemesView.as_view()),
    path("newmeme/", views.UserMemeView.as_view()),
    path("meme/<int:id>/", views.UserMemeView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)