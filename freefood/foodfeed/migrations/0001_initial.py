# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.TextField(default='NA')),
                ('organizer1', models.TextField(default='NA')),
                ('organizer2', models.TextField(default='NA')),
                ('organizer3', models.TextField(default='NA')),
                ('organizer4', models.TextField(default='NA')),
                ('organizer5', models.TextField(default='NA')),
                ('organizer6', models.TextField(default='NA')),
                ('organizer7', models.TextField(default='NA')),
                ('organizer8', models.TextField(default='NA')),
                ('organizer9', models.TextField(default='NA')),
                ('organizer10', models.TextField(default='NA')),
                ('venue_st1', models.TextField(default='NA')),
                ('venue_st2', models.TextField(default='NA')),
                ('zip_code', models.IntegerField(default=0)),
                ('venue_city', models.TextField(default='NA')),
                ('venue_state', models.TextField(default='NA')),
                ('venue_country', models.TextField(default='NA')),
                ('description', models.TextField(default='NA')),
                ('time1start', models.TextField(default='2015-09-01-17-30')),
                ('time2', models.TextField(default='2015-09-01-17-30')),
                ('time3', models.TextField(default='2015-09-01-17-30')),
            ],
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
