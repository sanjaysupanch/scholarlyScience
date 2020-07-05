from allauth.account.views import confirm_email
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
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
