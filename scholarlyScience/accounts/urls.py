from django.urls import include, path
from .import views
from .views import *


urlpatterns = [
    path('dummy/user/', UserList.as_view()),
    path('dummy/id/',  UserIdList.as_view()),
    path('dummy/user/<id>/', UserUpdateList.as_view()),
    path('dummy/user-profile-get/', UserProfileView.as_view()),
    path('dummy/profile/', ProfileView.as_view()),
    path('dummy/profile/<id>/', ProfileUpdateView.as_view()),
    path('dummy/email/<email>/', views.First_time),

]