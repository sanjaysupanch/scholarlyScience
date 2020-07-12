from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token 
# from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_auth.urls')),
    path('api/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('index.urls')),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
