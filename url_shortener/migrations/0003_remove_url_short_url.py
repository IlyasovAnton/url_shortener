# Generated by Django 3.2 on 2021-04-15 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20210415_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
    ]
