# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('summary', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to=b'photos')),
                ('picture', models.ImageField(upload_to=b'photos')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
