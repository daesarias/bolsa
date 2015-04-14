# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appi', '0002_auto_20150406_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(default=b'En espera', max_length=30),
            preserve_default=True,
        ),
    ]
