# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0007_auto_20160129_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklog',
            name='bind_host',
            field=models.ForeignKey(to='hosts.BindHostToUser'),
        ),
    ]
