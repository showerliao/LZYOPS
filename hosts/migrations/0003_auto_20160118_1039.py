# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20160118_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='posation',
            new_name='position',
        ),
    ]
