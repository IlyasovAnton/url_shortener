from rest_framework import serializers

from url_shortener.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'short_url']
