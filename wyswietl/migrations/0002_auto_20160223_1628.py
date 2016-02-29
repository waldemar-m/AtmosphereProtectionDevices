# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='odbiorca',
            name='obroty',
            field=models.CharField(default=datetime.datetime(2016, 2, 23, 16, 27, 22, 1716, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='odbiorca',
            name='strumien',
            field=models.CharField(default=(1, 1, 1), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='odbiorca',
            name='wysokosc',
            field=models.CharField(default=(1, 1, 1), max_length=20),
            preserve_default=False,
        ),
    ]
