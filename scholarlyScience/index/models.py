from django.db import models
from django.db.models import *
from django_mysql.models import *
from accounts.models import *

class company(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    remote = models.BooleanField(default=False)
    company_logo = models.URLField()
    No_of_Assignments = models.IntegerField()
    if_updated = BooleanField(default=True)
    No_of_Openings = models.IntegerField()
    tags = ListTextField(base_field=CharField(max_length=100), default="")
    Description = models.TextField(default="")
    tech_stack = ListTextField(base_field=CharField(max_length=100), default="")
    openings_tags = ListTextField(base_field=CharField(max_length=100), default="")
    location = ListTextField(base_field=CharField(max_length=100), default="")

class assessment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_logo = models.URLField()
    tech_stack = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    c_type  = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    date=models.DateField()
    
    