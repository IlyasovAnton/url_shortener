from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from url_shortener.models import URL
from url_shortener.serializers import URLSerializer
from url_shortener.util import fill_csv


class URLListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = URLSerializer
    queryset = URL.objects.all()


class URLShortener(APIView):
    def post(self, request: Request) -> Response:
        """
        The 'request' parameter 'data' must be in the type of
            {
             "url": "https://www.django-rest-framework.org/"
            }
        """
        url, _ = URL.objects.get_or_create(url=request.data['url'])
        return Response(url.short_url)


class URLView(APIView):
    def get(self, request: Request, hash: str) -> HttpResponseRedirect:
        url = get_object_or_404(URL, url_hash=hash)
        return HttpResponseRedirect(redirect_to=url.url)


class URLExport(APIView):
    def get(self, request: Request) -> HttpResponse:
        """
        the response is configured in such a way
        that the expected content of the response will be downloaded
        """
        response = HttpResponse(content_type='text\csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        fill_csv(response)
        return response
