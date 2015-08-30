# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0002_auto_20150830_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontype',
            name='profile_update',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 8, 30, 17, 14, 54, 382900, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persontype',
            name='signed_up',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 8, 30, 17, 15, 15, 873547, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
