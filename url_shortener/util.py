import csv
from base64 import urlsafe_b64encode
from uuid import uuid1

from django.http import HttpResponse

from url_shortener import models


def generate_hash() -> str:
    """
    Generate hash for short url.
    The hash calculation doesn't require a url
    but instead uses the system function uuid
    """
    hash = urlsafe_b64encode(uuid1().bytes)[:10]
    return hash.decode(encoding='utf-8')


def fill_csv(response: HttpResponse) -> None:
    """
    Create and fill to the HttpResponse 'response'
    """
    writer = csv.writer(response)
    [writer.writerow([url.url, url.short_url]) for url in list(models.URL.objects.all())]
