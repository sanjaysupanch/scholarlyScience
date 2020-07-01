from django.db import models
from django.contrib.auth.models import *
from django.conf import *
from django.contrib.auth.models import User



class User(AbstractUser):
	first_name = models.CharField(max_length=128, null=True)
	phone_number=models.CharField(max_length=13, unique=True)
	def __str__(self):
		return self.email
