from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        # Add custom password validation checks
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        # if password != confirm_password:
        #     raise ValueError('Passwords do not match')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, email, password, **extra_fields)

# Create your models here.
class CustomUser(AbstractUser):
    USER_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'))
    status = models.CharField(max_length=10, choices=USER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    objects = CustomUserManager()

CustomUser._meta.get_field('groups').related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').related_name = 'customuser_user_permissions'


class BlogCategory(models.Model):
    # CATEGORY_CHOICES = [
    #     ('Mental Health', 'Mental Health'),
    #     ('Heart Disease', 'Heart Disease'),
    #     ('Covid19', 'Covid19'),
    #     ('Immunization', 'Immunization'),
    # ]
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images', blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def truncated_summary(self):
        words = self.summary.split()[:15]
        return ' '.join(words) + ('...' if len(words) < len(self.summary.split()) else '')

    def __str__(self):
        return self.title

class Appointment(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient')
    date = models.DateField()
    start_time = models.TimeField()
    speciality = models.CharField(max_length=500)