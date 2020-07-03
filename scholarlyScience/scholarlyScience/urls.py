from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from index import views

router=routers.DefaultRouter()
router.register(r'companyauth',views.companiesviewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('index.urls')),
    path('',include(router.urls)),
    path('companies',include('rest_framework.urls',namespace='rest_framework'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
