from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from url_shortener.views import URLView, URLListViewSet, URLShortener, URLExport

router = DefaultRouter()
router.register('', URLListViewSet)

urlpatterns = [
    path(route='shortener/', view=URLShortener.as_view(), name='shortener'),
    path(route='export/', view=URLExport.as_view(), name='export'),
    re_path(route=r'^(?P<hash>.+)$', view=URLView.as_view(), name='view'),
]

urlpatterns += router.urls
