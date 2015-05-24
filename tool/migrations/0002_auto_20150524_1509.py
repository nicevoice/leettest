# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '__first__'),
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='tags',
            field=models.ManyToManyField(to='public.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
