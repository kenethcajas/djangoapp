# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('marca1', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('modelo1', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(upload_to='photo')),
                ('marca', models.ForeignKey(to='proyfinvehiculos.Marca')),
                ('modelo', models.ForeignKey(to='proyfinvehiculos.Modelo')),
            ],
        ),
    ]
