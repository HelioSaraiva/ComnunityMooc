# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170401_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=0, verbose_name='Situação'),
        ),
    ]
