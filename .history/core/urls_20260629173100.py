from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # مسیرهای allauth
    path('', include('accounts.urls')),  # مسیرهای اپ accounts
]