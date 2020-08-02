from django.shortcuts import render
from accounts.models import *
from accounts.serializers import *
from accounts.models import CustomUser
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import HttpResponse


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserIdList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)


class UserUpdateList(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'id'


class UserProfileView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer


class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        email = self.request.user
        user_instance = CustomUser.objects.get(email=email)

        serializer.save(customuser=user_instance)


class ProfileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

    # def perform_update(self, serializer):
    #     email = self.request.user
    #     user_instance = CustomUser.objects.get(email=email)
    #     serializer.save(Profile.objects.get(customuser=user_instance))

# class First_time(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     # serializer_class = First_time_Serializer

#     def get_queryset(self):
#         email= self.kwargs['email']
#         user_instance = CustomUser.objects.get(email=email)
#         temp = Profile.objects.filter(customuser=user_instance)
#         if (temp.first_time_login == True):
#             return 1
#         else:
#             return 0


def First_time(request, **kwargs):
    email = kwargs['email']
    try:
        user_instance = CustomUser.objects.get(email=email)
        temp = Profile.objects.get(customuser=user_instance)
        
        if (temp.first_time_login == True):
            data={'first_time':1}
            return JsonResponse(data)
        else:
            data={'first_time':0}
            return JsonResponse(data)
    except:
        try:
            CustomUser.objects.get(email=email)
            data={'first_time':0}
            return JsonResponse(data)
            
        except:
            data={'first_time':3}
            return JsonResponse(data)
