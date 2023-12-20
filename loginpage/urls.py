from django.urls import path
from . import views

urlpatterns = [
    path("",views.display,name="display"),
    path("register/",views.register_page,name="register"),
    path("login/",views.login_page,name="login"),
    path("literature/",views.display, name="literature")
]
