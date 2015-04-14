# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appi', '0003_auto_20150406_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default=b'Indefinido', max_length=30),
            preserve_default=True,
        ),
    ]
