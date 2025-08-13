from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(unique=True, max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=False, max_length=50)
    gender = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)
    school_name = models.CharField(max_length=10)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)
    father_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)   

    def __str__(self):
        return self.name
    



class StudentManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username)
        user.set_password(password)
        if email:
            user.email = self.normalize_email(email)
        user.is_active = True
        user.is_staff = False
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, password=None, email=None):
        user = self.create_user(username, password, email)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    
    def get_by_natural_key(self, username):
        return self.get(username = username) 

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

class studentUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    # Required fields for the custom user model
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = StudentManager()

    def __str__(self):
        return self.username


class StudentProfile(models.Model):
    user = models.OneToOneField(studentUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)
    school_name = models.CharField(max_length=10)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)
    father_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
    
