from django.contrib import admin

from url_shortener.models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('url', 'short_url')
    list_display_links = ('url', 'short_url')
    readonly_fields = ('url_hash', 'short_url')
    list_per_page = 15
