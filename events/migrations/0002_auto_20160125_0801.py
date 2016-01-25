# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='managing'),
        ),
        migrations.AddField(
            model_name='events',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='participating'),
        ),
        migrations.AddField(
            model_name='events',
            name='winners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='winnings'),
        ),
    ]
