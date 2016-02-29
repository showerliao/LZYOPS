# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20160120_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('done_time', models.DateTimeField(null=True, blank=True)),
                ('task_type', models.CharField(max_length=50, choices=[(b'cmd', b'CMD'), (b'file_send', b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0'), (b'file_get', b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd')])),
                ('cmd', models.TextField()),
                ('expire_time', models.IntegerField(default=30)),
                ('task_pid', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u6279\u91cf\u4efb\u52a1',
                'verbose_name_plural': '\u6279\u91cf\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event_log', models.TextField()),
                ('result', models.CharField(default=b'Unknown', max_length=30, choices=[(b'success', b'Success'), (b'failed', b'Failed'), (b'unknown', b'Unknown')])),
                ('note', models.TextField(max_length=100, blank=True)),
            ],
            options={
                'verbose_name': '\u6279\u91cf\u4efb\u52a1\u65e5\u5fd7',
                'verbose_name_plural': '\u6279\u91cf\u4efb\u52a1\u65e5\u5fd7',
            },
        ),
        migrations.AlterModelOptions(
            name='bindhosttouser',
            options={'verbose_name': '\u4e3b\u673a\u4e0e\u7528\u6237\u7684\u7ed1\u5b9a\u5173\u7cfb', 'verbose_name_plural': '\u4e3b\u673a\u4e0e\u7528\u6237\u7684\u7ed1\u5b9a\u5173\u7cfb'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': '\u4e3b\u673a', 'verbose_name_plural': '\u4e3b\u673a'},
        ),
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'verbose_name': '\u4e3b\u673a\u7ec4', 'verbose_name_plural': '\u4e3b\u673a\u7ec4'},
        ),
        migrations.AlterModelOptions(
            name='hostuser',
            options={'verbose_name': '\u4e3b\u673a\u7528\u6237', 'verbose_name_plural': '\u4e3b\u673a\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='idc',
            options={'verbose_name': 'IDC\u673a\u623f', 'verbose_name_plural': 'IDC\u673a\u623f'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='host',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='host',
            name='host_name',
            field=models.CharField(max_length=64, verbose_name='\u4e3b\u673a\u540d'),
        ),
        migrations.AlterField(
            model_name='host',
            name='ip_addr',
            field=models.GenericIPAddressField(unique=True, verbose_name='IP\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='host',
            name='memo',
            field=models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='port',
            field=models.IntegerField(default=22, verbose_name='\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='host',
            name='system_type',
            field=models.CharField(default=b'linux', max_length=32, verbose_name='\u7cfb\u7edf\u7c7b\u578b', choices=[(b'linux', b'Linux'), (b'windows', b'Windows')]),
        ),
        migrations.AlterField(
            model_name='idc',
            name='memo',
            field=models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='bind_hosts',
            field=models.ManyToManyField(to='hosts.BindHostToUser', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosttouser',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='bind_host',
            field=models.ForeignKey(to='hosts.Host'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='child_of_task',
            field=models.ForeignKey(to='hosts.TaskInfo'),
        ),
        migrations.AddField(
            model_name='taskinfo',
            name='hosts',
            field=models.ForeignKey(to='hosts.BindHostToUser'),
        ),
        migrations.AddField(
            model_name='taskinfo',
            name='user',
            field=models.ForeignKey(to='hosts.HostUser'),
        ),
    ]
