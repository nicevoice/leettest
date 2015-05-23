# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestBug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('execute_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('execute_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('website', models.CharField(max_length=50, blank=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='testcase',
            name='testcycle',
            field=models.ForeignKey(to='crowd.TestCycle'),
        ),
        migrations.AddField(
            model_name='testbug',
            name='testcycle',
            field=models.ForeignKey(to='crowd.TestCycle'),
        ),
    ]
