
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        # Add custom password validation checks
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if password != confirm_password:
            raise ValueError('Passwords do not match')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.
class CustomUser(AbstractUser):
    USER_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'))
    status = models.CharField(max_length=10, choices=USER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    objects = CustomUserManager()

CustomUser._meta.get_field('groups').related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').related_name = 'customuser_user_permissions'
