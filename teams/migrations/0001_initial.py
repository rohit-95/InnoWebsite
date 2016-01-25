# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('captain', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='member')),
            ],
        ),
    ]
