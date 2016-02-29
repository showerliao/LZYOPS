# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_auto_20160118_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='BindHostToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_name', models.CharField(max_length=64)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('port', models.IntegerField(default=22)),
                ('system_type', models.CharField(default=b'linux', max_length=32, choices=[(b'linux', b'Linux'), (b'windows', b'Windows')])),
                ('enabled', models.BooleanField(default=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_type', models.CharField(default=b'ssh-password', max_length=64, choices=[(b'ssh-password', b'SSH/PASSWORD'), (b'ssh-key', b'SSH/KEY')])),
                ('user_name', models.CharField(unique=True, max_length=64)),
                ('password', models.CharField(max_length=128, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 8, 1, 48, 240209, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='memo',
            field=models.TextField(default=None, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(default=None, max_length=32, null=True, verbose_name='\u624b\u673a', blank=True),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(to='hosts.IDC'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host',
            field=models.ForeignKey(to='hosts.Host'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host_groups',
            field=models.ManyToManyField(to='hosts.HostGroup'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host_user',
            field=models.ForeignKey(to='hosts.HostUser'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='bind_hosts',
            field=models.ManyToManyField(default=datetime.datetime(2016, 1, 20, 8, 0, 33, 285816, tzinfo=utc), to='hosts.BindHostToUser', blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='host_groups',
            field=models.ManyToManyField(to='hosts.HostGroup', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosttouser',
            unique_together=set([('host', 'host_user')]),
        ),
    ]
