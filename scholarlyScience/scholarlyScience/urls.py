# from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_auth.urls')),
    path('api/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('index.urls')),
    path('login/', obtain_jwt_token),
    # path('accounts-rest/registration/account-confirm-email/<pk>/', confirm_email, name='account_confirm_email'),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
