from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', admin.site.urls),
    path(r'', include('crudapp.urls')),
]

handler404 = 'crudapp.views.error_404_view'
