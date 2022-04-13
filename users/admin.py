from atexit import register
from django.contrib import admin
from users.models import CustomUser


class UserModel(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'date_joined', 'is_staff', 'is_active', 'is_superuser')
    
admin.site.register(CustomUser, UserModel)