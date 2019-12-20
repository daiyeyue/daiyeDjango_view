# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=datetime.datetime(2019, 12, 20, 3, 11, 15, 175306, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
