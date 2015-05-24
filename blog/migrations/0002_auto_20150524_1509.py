# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='readcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='caption',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='subcaption',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
