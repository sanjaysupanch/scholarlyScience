from django.db import models


class companies(models.Model):
    bgImage = models.TextField()
    companyName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)
    

class skill(models.Model):
    companie=models.ForeignKey(companies, related_name='cskill',  on_delete=models.CASCADE)
    skills=models.CharField(max_length=50) 
