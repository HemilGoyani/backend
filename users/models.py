from django.db import models  
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  



class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using= self._db)
        return user


    def create_superuser(self, email, username, password):    
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
  
        user.is_staff =True
        user.is_superuser = True
        user.save(using= self._db)
        return user


class User(AbstractBaseUser):  
    username = models.CharField(max_length = 20,unique=True)  
    email = models.EmailField(unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now) 
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    is_superuser = models.BooleanField(default=True)
  
  
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    objects = UserManager()

    def __str__(self):
        return self.email
  
      
    def has_perm(self, perm, obj=None):    
        return self.is_superuser
  
    def has_module_perms(self, app_label):  
        return True