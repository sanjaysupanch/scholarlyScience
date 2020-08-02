from django.urls import include, path
from .import views
from .views import *



urlpatterns = [
    path('company/', CompanyView.as_view(), name='company-api'),
    path('company-list/', CompanyListView.as_view(), name='company-list'),
    path('company/<id>/', CompanyUpdateView.as_view()),
    path('assessment/', AssessmentView.as_view(), name='assessment-api'),
    path('assessment-list/', AssessmentListView.as_view(), name='assessment-list'),
    path('whatsapp/', whatsappview.as_view()),
    path('whatsapp/<id>/', whatsappupdateview.as_view()),
]