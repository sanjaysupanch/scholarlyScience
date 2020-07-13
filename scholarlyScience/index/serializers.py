from accounts.models import CustomUser
from .models import *
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=company
        fields=['company_name', 'company_logo', 'No_of_Assignments', 'if_updated', 'No_of_Openings', 'tags', 'Description', 'tech_stack', 'openings_tags', 'remote', 'location']

class CompanyListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=company
        fields=['company_name', 'company_logo', 'No_of_Assignments','No_of_Openings', 'tech_stack', 'location']


class AssesmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=assessment
        fields=['company_logo', 'tech_stack', 'company_name', 'job_type', 'location', 'date']


class AssesmentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=assessment
        fields=['company_logo', 'tech_stack', 'company_name', 'job_type', 'location', 'date']
