from django.contrib.auth.models import User
from .models import companies
from rest_framework import serializers

class companiesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=companies
        fields=["bgImage","companyName","location","assignment","jobs"]