from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(route='admin/', view=admin.site.urls, name='admin'),
    path('', include('url_shortener.urls'))
]
