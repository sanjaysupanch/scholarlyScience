from django.urls import include, path
from .import views
from .views import *



urlpatterns = [
    path('company/', CompanyView.as_view(), name='company-api'),
    path('company-list/', CompanyListView.as_view(), name='company-list'),
]