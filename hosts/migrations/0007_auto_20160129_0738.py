# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0006_auto_20160129_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskinfo',
            name='hosts',
        ),
        migrations.AddField(
            model_name='taskinfo',
            name='hosts',
            field=models.ManyToManyField(to='hosts.BindHostToUser'),
        ),
    ]
