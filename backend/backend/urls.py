from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.articles.urls')),
    path('api/', include('apps.authentication.urls')),
    path('api/', include('apps.comments.urls')),
]