from django.db import models
from django.db.models import *
from accounts.models import *
from django.contrib.postgres.fields import ArrayField

class company(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    remote = models.BooleanField(default=False)
    company_logo = models.URLField()
    No_of_Assignments = models.IntegerField(null=True)
    if_updated = BooleanField(default=True)
    No_of_Openings = models.IntegerField(null=True)
    tags = ArrayField(
            models.CharField(max_length=5000, blank=True),blank=True
        )
    Description = models.TextField(default="")
    location = ArrayField(
            models.CharField(max_length=5000, blank=True),blank=True
        )

class assessment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_logo = models.URLField()
    tech_stack = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_type  = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    date=models.DateField()
    

class whatsapp(models.Model):
    link = models.URLField() 