# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0005_auto_20160129_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='task_type',
            field=models.CharField(max_length=50, choices=[(b'multi_cmd', b'CMD'), (b'file_send', b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0'), (b'file_get', b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd')]),
        ),
    ]
