from django.shortcuts import render, redirect
from accounts.models import *
from index.models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import *
from .serializers import  *
from rest_framework.permissions import IsAdminUser
import csv

class CompanyView(generics.ListCreateAPIView):
    queryset=company.objects.all()
    serializer_class=CompanySerializer

    def get_queryset(self):
        email = self.request.user
        user_instance = CustomUser.objects.get(email=email)
        return company.objects.filter(user=user_instance)
    
    def perform_create(self,serializer):
        email = self.request.user
        user_instance = CustomUser.objects.get(email=email)
        serializer.save(user=user_instance)


class CompanyListView(generics.ListAPIView):
    queryset=company.objects.all()
    serializer_class=CompanyListSerializer


class CompanyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=company.objects.all()
    serializer_class=CompanySerializer
    # permission_classes = [IsAdminUser]
    lookup_field='id'


class AssessmentView(generics.ListCreateAPIView):
    queryset=assessment.objects.all()
    serializer_class=AssesmentSerializer

    def get_queryset(self):
        email = self.request.user
        user_instance = CustomUser.objects.get(email=email)
        return assessment.objects.filter(user=user_instance)

    def perform_create(self,serializer):
        email = self.request.user
        user_instance = CustomUser.objects.get(email=email)
        serializer.save(user=user_instance)


class AssessmentListView(generics.ListAPIView):
    queryset=assessment.objects.all()
    serializer_class=AssesmentListSerializer

class whatsappview(generics.ListCreateAPIView):
    queryset = whatsapp.objects.all()
    serializer_class = whatsappSerializer

class whatsappupdateview(generics.RetrieveUpdateDestroyAPIView):
    queryset = whatsapp.objects.all()
    serializer_class = whatsappSerializer
    lookup_field = 'id'

# def csvs(request):
#     with open('/home/san/db.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
            
#             if line_count == 0:
#                 print(f'{", ".join(row)}')

#                 line_count += 1
            
#             else:
#                 company.objects.create(user=request.user, company_name=row[1], company_logo=row[2], tags=row[3], Description=row[4], No_of_Assignments=row[6], No_of_Openings=row[7], if_updated=True, location=row[9], remote=True)
#                 line_count += 1
#         print(line_count, '\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

#     return redirect('/san/')
