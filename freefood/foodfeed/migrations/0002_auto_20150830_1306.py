# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='time1end',
            field=models.TextField(default='2015-09-01-17-30'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='time2end',
            field=models.TextField(default='2015-09-01-17-30'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='time3end',
            field=models.TextField(default='2015-09-01-17-30'),
        ),
    ]
