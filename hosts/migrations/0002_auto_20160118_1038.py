# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='department',
            field=models.CharField(default=None, max_length=64, null=True, verbose_name='\u90e8\u95e8', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='job_number',
            field=models.IntegerField(default=None, null=True, verbose_name='\u5de5\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(default=None, max_length=64, null=True, verbose_name='\u59d3\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='posation',
            field=models.CharField(default=None, max_length=64, null=True, verbose_name='\u804c\u4f4d', blank=True),
        ),
    ]
