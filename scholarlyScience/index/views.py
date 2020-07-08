from django.shortcuts import render, redirect
from accounts.models import *
from index.models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import * 
from .serializers import  *


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
   