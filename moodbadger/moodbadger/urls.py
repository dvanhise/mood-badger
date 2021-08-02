from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('mood.urls')),
    path('admin/', admin.site.urls),
    path(r'rest-auth/', include('rest_auth.urls')),
    # path('auth/', include('rest_framework.urls')),
]
