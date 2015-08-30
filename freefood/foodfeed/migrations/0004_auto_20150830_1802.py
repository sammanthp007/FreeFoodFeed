# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0003_auto_20150830_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtype',
            name='time1end',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='time1start',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='time2end',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='time3',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='time3end',
        ),
        migrations.AddField(
            model_name='eventtype',
            name='date1',
            field=models.TextField(default='2015-09-01'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='date2',
            field=models.TextField(default='2015-09-01'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='foodtype',
            field=models.TextField(default='light refreshment'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='time1',
            field=models.TextField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='time2',
            field=models.TextField(default='00:00'),
        ),
    ]
