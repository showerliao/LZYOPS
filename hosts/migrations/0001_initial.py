# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('job_number', models.IntegerField(default=None, verbose_name='\u5de5\u53f7', blank=True)),
                ('name', models.CharField(default=None, max_length=64, verbose_name='\u59d3\u540d', blank=True)),
                ('department', models.CharField(default=None, max_length=64, verbose_name='\u90e8\u95e8', blank=True)),
                ('posation', models.CharField(default=None, max_length=64, verbose_name='\u804c\u4f4d', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
