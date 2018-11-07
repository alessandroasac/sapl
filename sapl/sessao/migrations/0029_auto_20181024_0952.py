# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-24 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0028_auto_20181024_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='justificativaausencia',
            name='materias_da_ordem_do_dia',
            field=models.ManyToManyField(blank=True, to='sessao.OrdemDia', verbose_name='Matérias do Ordem do Dia'),
        ),
        migrations.AddField(
            model_name='justificativaausencia',
            name='materias_do_expediente',
            field=models.ManyToManyField(blank=True, to='sessao.ExpedienteMateria', verbose_name='Matérias do Expediente'),
        ),
    ]