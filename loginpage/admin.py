from django.contrib import admin
from .models import RegisterUser,LoginUser,Sample
# Register your models here.
admin.site.register(RegisterUser)
admin.site.register(LoginUser)
admin.site.register(Sample)