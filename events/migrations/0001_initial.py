# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='event_pics/', blank=True)),
                ('min_participants', models.IntegerField(default=1)),
                ('is_team_event', models.BooleanField(default=False)),
            ],
        ),
    ]
