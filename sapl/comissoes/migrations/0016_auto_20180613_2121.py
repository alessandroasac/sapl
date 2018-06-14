# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-14 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comissoes', '0015_auto_20180613_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reuniao',
            name='periodo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='comissoes.Periodo', verbose_name='Periodo da Composicão da Comissão'),
        ),
    ]
