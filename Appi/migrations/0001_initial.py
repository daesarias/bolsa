# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('numero', models.CharField(unique=True, max_length=50)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=20, null=True, blank=True)),
                ('fecha_nacimiento', models.CharField(max_length=20, null=True, blank=True)),
                ('estado', models.CharField(default=b'En espera', max_length=30)),
                ('perfil', models.CharField(max_length=30, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
