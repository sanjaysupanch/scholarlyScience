from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name')
    

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name')


class AllauthSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Full Name')
    phone_number = forms.CharField(max_length=30, label='phone_number')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user