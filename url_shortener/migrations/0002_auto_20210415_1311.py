# Generated by Django 3.2 on 2021-04-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(),
        ),
    ]
