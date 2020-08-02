from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    full_name = models.CharField(blank=True, max_length=100)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.email


class Profile(models.Model):
    customuser = models.OneToOneField(CustomUser, related_name='userprofile', on_delete=models.CASCADE)
    city = models.CharField(max_length=80)
    location = models.CharField(max_length=60)
    college = models.CharField(max_length=120)
    degree = models.CharField(max_length=30)
    trade = models.CharField(max_length=40)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    
    preferences = ArrayField(
            models.CharField(max_length=5000, blank=True),blank=True
        )
    preference_role = ArrayField(
            models.CharField(max_length=5000, blank=True),blank=True
        )
    skills = ArrayField(
            models.CharField(max_length=5000, blank=True),blank=True
        )
    profession = models.IntegerField()
    share_profile = models.BooleanField(default=False)
    opportunities = models.BooleanField(default=False)
    linkedin = models.CharField(max_length=120, blank=True)
    github = models.CharField(max_length=120, blank=True)
    wechat = models.CharField(max_length=120, blank=True)
    lineid = models.CharField(max_length=120, blank=True)
    dribble = models.CharField(max_length=120, blank=True)
    portfolio = models.CharField(max_length=120, blank=True)
    first_time_login = models.BooleanField(default=False)
    