# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150524_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ispublic',
            field=models.BooleanField(default=1),
        ),
    ]
