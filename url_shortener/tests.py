from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from url_shortener.models import URL

client = Client()
url = 'https://www.django-rest-framework.org/api-guide/testing/'


class URLShortener(TestCase):
    def setUp(self) -> None:
        URL.objects.create(url=url)

    def test_shortener(self):
        response = client.post(reverse('shortener'))
        short_url = URL.objects.get(url=url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.text, short_url.short_url)

    def test_view(self):
        pass
        # response = client.post(reverse('shortener', kwargs={'hash': }))
