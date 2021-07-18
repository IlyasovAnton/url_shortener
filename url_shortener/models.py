from django.db import models
from url_shortener.util import generate_hash
from main_app.settings import HOST_NAME


class URL(models.Model):
    url = models.URLField()
    url_hash = models.CharField(max_length=10, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        """
        Save the current instance with calculating url hash
        """
        self.url_hash = generate_hash()
        super(URL, self).save(*args, **kwargs)

    @property
    def short_url(self):
        """
        Create short url using the calculated url hash
        """
        return HOST_NAME + self.url_hash
